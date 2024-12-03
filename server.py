import aiohttp
from aiohttp import web
import logging
import mimetypes
import asyncio
import uuid
import os
import hashlib
import execution
from app.user_manager import UserManager
import traceback
import nodes
from typing import Optional

output_directory = os.path.join(os.path.dirname(os.path.realpath(__file__)), "output")
temp_directory = os.path.join(os.path.dirname(os.path.realpath(__file__)), "temp")
input_directory = os.path.join(os.path.dirname(os.path.realpath(__file__)), "input")


async def send_socket_catch_exception(function, message):
    try:
        await function(message)
    except (
        aiohttp.ClientError,
        aiohttp.ClientPayloadError,
        ConnectionResetError,
    ) as err:
        logging.warning("send error: {}".format(err))


@web.middleware
async def cache_control(request: web.Request, handler):
    response: web.Response = await handler(request)
    if request.path.endswith(".js") or request.path.endswith(".css"):
        response.headers.setdefault("Cache-Control", "no-cache")
    return response


def create_cors_middleware(allowed_origin: str):
    @web.middleware
    async def cors_middleware(request: web.Request, handler):
        if request.method == "OPTIONS":
            # Pre-flight request. Reply successfully:
            response = web.Response()
        else:
            response = await handler(request)

        response.headers["Access-Control-Allow-Origin"] = allowed_origin
        response.headers["Access-Control-Allow-Methods"] = (
            "POST, GET, DELETE, PUT, OPTIONS"
        )
        response.headers["Access-Control-Allow-Headers"] = "Content-Type, Authorization"
        response.headers["Access-Control-Allow-Credentials"] = "true"
        return response

    return cors_middleware


class WorkflowServer:
    def __init__(self, loop):
        WorkflowServer.instance = self

        mimetypes.init()
        mimetypes.types_map[".js"] = "application/javascript; charset=utf-8"

        self.user_manager = UserManager()
        self.workflow_queue = None
        self.loop = loop
        self.messages = asyncio.Queue()
        self.client_session: Optional[aiohttp.ClientSession] = None
        self.number = 0

        middlewares = [cache_control]
        middlewares.append(create_cors_middleware("*"))

        max_upload_size = round(1 * 1024 * 1024)  # 1 MB
        self.app = web.Application(
            client_max_size=max_upload_size, middlewares=middlewares
        )
        self.sockets = dict()

        routes = web.RouteTableDef()
        self.routes = routes
        self.last_node_id = None
        self.client_id = None

        self.on_workflow_handlers = []

        self.web_root = os.path.join(os.path.dirname(os.path.realpath(__file__)), "web")

        @routes.get("/ws")
        async def websocket_handler(request):
            ws = web.WebSocketResponse()
            await ws.prepare(request)
            sid = request.rel_url.query.get("clientId", "")
            if sid:
                # Reusing existing session, remove old
                self.sockets.pop(sid, None)
            else:
                sid = uuid.uuid4().hex

            self.sockets[sid] = ws

            try:
                # Send initial state to the new client
                await self.send(
                    "status", {"status": self.get_queue_info(), "sid": sid}, sid
                )
                # On reconnect if we are the currently executing client send the current node
                if self.client_id == sid and self.last_node_id is not None:
                    await self.send("executing", {"node": self.last_node_id}, sid)

                async for msg in ws:
                    if msg.type == aiohttp.WSMsgType.ERROR:
                        logging.warning(
                            "ws connection closed with exception %s" % ws.exception()
                        )
            finally:
                self.sockets.pop(sid, None)
            return ws

        # TODO : will make custom frontend later
        @routes.get("/")
        async def get_root(request: web.Request):
            return web.FileResponse(os.path.join(self.web_root, "index.html"))

        def compare_file_hash(filepath, file):
            hasher = hashlib.md5

            # function to compare hashes of two images to see if it already exists, fix to #3465
            if os.path.exists(filepath):
                a = hasher()
                b = hasher()
                with open(filepath, "rb") as f:
                    a.update(f.read())
                    b.update(file.file.read())
                    file.file.seek(0)
                    f.close()
                return a.hexdigest() == b.hexdigest()
            return False

        def get_dir_by_type(dir_type):
            if dir_type is None:
                dir_type = "input"

            if dir_type == "input":
                type_dir = input_directory
            elif dir_type == "temp":
                type_dir = temp_directory
            elif dir_type == "output":
                type_dir = output_directory

            return type_dir, dir_type

        def file_upload(post):
            file = post.get("file")
            file_is_duplicate = False

            file_upload_type = post.get("type")
            upload_dir, image_upload_type = get_dir_by_type(file_upload_type)

            if file and file.file:
                filename = file.filename
                if not filename:
                    return web.Response(status=400)

                subfolder = post.get("subfolder", "")
                full_output_folder = os.path.join(
                    upload_dir, os.path.normpath(subfolder)
                )
                filepath = os.path.abspath(os.path.join(full_output_folder, filename))

                if os.path.commonpath((upload_dir, filepath)) != upload_dir:
                    return web.Response(status=400)

                if not os.path.exists(full_output_folder):
                    os.makedirs(full_output_folder)

                split = os.path.splitext(filename)

                i = 1
                while os.path.exists(filepath):
                    if compare_file_hash(
                        filepath, file
                    ):  # compare hash to prevent saving of duplicates with same name, fix for #3465
                        file_is_duplicate = True
                        break
                    filename = f"{split[0]}_({i}){split[1]}"
                    filepath = os.path.join(full_output_folder, filename)
                    i += 1

                if not file_is_duplicate:
                    with open(filepath, "wb") as f:
                        f.write(file.file.read())

                return web.json_response(
                    {
                        "name": filename,
                        "subfolder": subfolder,
                        "type": image_upload_type,
                    }
                )

        @routes.post("/upload/file")
        async def upload_file(request):
            post = await request.post()
            return file_upload(post)

        @routes.get("/workflow")
        async def get_workflow(request):
            return web.json_response(self.get_queue_info())

        @routes.post("/workflow")
        async def post_workflow(request):
            logging.info("Got Workflow")
            resp_code = 200
            out_string = ""
            json_data = await request.json()
            json_data = self.trigger_on_workflow(json_data)

            if "number" in json_data:
                number = float(json_data["number"])
            else:
                number = self.number
                if "front" in json_data:
                    if json_data["front"]:
                        number = -number

                self.number += 1

            if "workflow" in json_data:
                workflow = json_data["workflow"]
                valid = execution.validate_workflow(workflow)
                extra_data = {}
                if "extra_data" in json_data:
                    extra_data = json_data["extra_data"]

                if "client_id" in json_data:
                    extra_data["client_id"] = json_data["client_id"]
                if valid[0]:
                    workflow_id = str(uuid.uuid4())
                    outputs_to_execute = valid[2]
                    self.workflow_queue.put(
                        (number, workflow_id, workflow, extra_data, outputs_to_execute)
                    )
                    response = {
                        "workflow_id": workflow_id,
                        "number": number,
                        "node_errors": valid[3],
                    }
                    return web.json_response(response)
                else:
                    logging.warning("invalid workflow: {}".format(valid[1]))
                    return web.json_response(
                        {"error": valid[1], "node_errors": valid[3]}, status=400
                    )
            else:
                return web.json_response(
                    {"error": "no workflow", "node_errors": []}, status=400
                )

        def node_info(node_class):
            obj_class = nodes.NODE_CLASS_MAPPINGS[node_class]
            info = {}
            info["input"] = obj_class.INPUT_TYPES()
            info["input_order"] = {
                key: list(value.keys())
                for (key, value) in obj_class.INPUT_TYPES().items()
            }
            info["output"] = obj_class.RETURN_TYPES
            info["output_is_list"] = (
                obj_class.OUTPUT_IS_LIST
                if hasattr(obj_class, "OUTPUT_IS_LIST")
                else [False] * len(obj_class.RETURN_TYPES)
            )
            info["output_name"] = (
                obj_class.RETURN_NAMES
                if hasattr(obj_class, "RETURN_NAMES")
                else info["output"]
            )
            info["name"] = node_class
            info["display_name"] = (
                nodes.NODE_DISPLAY_NAME_MAPPINGS[node_class]
                if node_class in nodes.NODE_DISPLAY_NAME_MAPPINGS.keys()
                else node_class
            )
            info["description"] = (
                obj_class.DESCRIPTION if hasattr(obj_class, "DESCRIPTION") else ""
            )
            info["python_module"] = getattr(
                obj_class, "RELATIVE_PYTHON_MODULE", "nodes"
            )
            info["category"] = "sd"
            if hasattr(obj_class, "OUTPUT_NODE") and obj_class.OUTPUT_NODE == True:
                info["output_node"] = True
            else:
                info["output_node"] = False

            if hasattr(obj_class, "CATEGORY"):
                info["category"] = obj_class.CATEGORY

            if hasattr(obj_class, "OUTPUT_TOOLTIPS"):
                info["output_tooltips"] = obj_class.OUTPUT_TOOLTIPS

            if getattr(obj_class, "DEPRECATED", False):
                info["deprecated"] = True
            if getattr(obj_class, "EXPERIMENTAL", False):
                info["experimental"] = True
            return info

        @routes.get("/object_info")
        async def get_object_info(request):
            out = {}
            for x in nodes.NODE_CLASS_MAPPINGS:
                try:
                    out[x] = node_info(x)
                except Exception as e:
                    logging.error(
                        f"[ERROR] An error occurred while retrieving information for the '{x}' node."
                    )
                    logging.error(traceback.format_exc())
            return web.json_response(out)

        @routes.get("/object_info/{node_class}")
        async def get_object_info_node(request):
            node_class = request.match_info.get("node_class", None)
            out = {}
            if (node_class is not None) and (node_class in nodes.NODE_CLASS_MAPPINGS):
                out[node_class] = node_info(node_class)
            return web.json_response(out)

        @routes.get("/history")
        async def get_history(request):
            max_items = request.rel_url.query.get("max_items", None)
            if max_items is not None:
                max_items = int(max_items)
            return web.json_response(
                self.workflow_queue.get_history(max_items=max_items)
            )

        @routes.get("/history/{workflow_id}")
        async def get_history(request):
            workflow_id = request.match_info.get("workflow_id", None)
            return web.json_response(
                self.workflow_queue.get_history(workflow_id=workflow_id)
            )

        @routes.get("/queue")
        async def get_queue(request):
            queue_info = {}
            current_queue = self.workflow_queue.get_current_queue()
            queue_info["queue_running"] = current_queue[0]
            queue_info["queue_pending"] = current_queue[1]
            return web.json_response(queue_info)

        @routes.post("/interrupt")
        async def post_interrupt(request):
            nodes.interrupt_processing()
            return web.Response(status=200)

        @routes.post("/history")
        async def post_history(request):
            json_data = await request.json()
            if "clear" in json_data:
                if json_data["clear"]:
                    self.workflow_queue.wipe_history()
            if "delete" in json_data:
                to_delete = json_data["delete"]
                for id_to_delete in to_delete:
                    self.workflow_queue.delete_history_item(id_to_delete)

            return web.Response(status=200)

    async def setup(self):
        timeout = aiohttp.ClientTimeout(total=None)  # no timeout
        self.client_session = aiohttp.ClientSession(timeout=timeout)

    def add_routes(self):
        self.user_manager.add_routes(self.routes)
        # self.app.add_subapp("/internal", self.internal_routes.get_app())

        # Prefix every route with /api for easier matching for delegation.
        # This is very useful for frontend dev server, which need to forward
        # everything except serving of static files.
        # Currently both the old endpoints without prefix and new endpoints with
        # prefix are supported.
        api_routes = web.RouteTableDef()
        for route in self.routes:
            # Custom nodes might add extra static routes. Only process non-static
            # routes to add /api prefix.
            if isinstance(route, web.RouteDef):
                api_routes.route(route.method, "/api" + route.path)(
                    route.handler, **route.kwargs
                )
        self.app.add_routes(api_routes)
        self.app.add_routes(self.routes)

        # for name, dir in nodes.EXTENSION_WEB_DIRS.items():
        #     self.app.add_routes(
        #         [
        #             web.static("/extensions/" + urllib.parse.quote(name), dir),
        #         ]
        #     )

        self.app.add_routes(
            [
                web.static("/", self.web_root),
            ]
        )

    async def send(self, event, data, sid=None):
        # if event == BinaryEventTypes.UNENCODED_PREVIEW_IMAGE:
        #     await self.send_image(data, sid=sid)
        # elif isinstance(data, (bytes, bytearray)):
        #     await self.send_bytes(event, data, sid)
        # else:
        #     await self.send_json(event, data, sid)
        await self.send_json(event, data, sid)

    def send_sync(self, event, data, sid=None):
        self.loop.call_soon_threadsafe(self.messages.put_nowait, (event, data, sid))

    def queue_updated(self):
        self.send_sync("status", {"status": self.get_queue_info()})

    def get_queue_info(self):
        workflow_info = {}
        exec_info = {}
        # exec_info["queue_remaining"] = self.workflow_queue.get_tasks_remaining()
        workflow_info["exec_info"] = exec_info
        return workflow_info

    async def send_json(self, event, data, sid=None):
        message = {"type": event, "data": data}

        if sid is None:
            sockets = list(self.sockets.values())
            for ws in sockets:
                await send_socket_catch_exception(ws.send_json, message)
        elif sid in self.sockets:
            await send_socket_catch_exception(self.sockets[sid].send_json, message)

    async def publish_loop(self):
        while True:
            msg = await self.messages.get()
            await self.send(*msg)

    async def start(self, address, port, verbose=True, call_on_start=None):
        runner = web.AppRunner(self.app, access_log=None)
        await runner.setup()
        ssl_ctx = None
        scheme = "http"
        site = web.TCPSite(runner, address, port, ssl_context=ssl_ctx)
        await site.start()

        self.address = address
        self.port = port

        if verbose:
            logging.info("Starting server\n")
            logging.info(
                "To see the GUI go to: {}://{}:{}".format(scheme, address, port)
            )
        if call_on_start is not None:
            call_on_start(scheme, address, port)

    def add_on_workflow_handler(self, handler):
        self.on_workflow_handlers.append(handler)

    def trigger_on_workflow(self, json_data):
        for handler in self.on_workflow_handlers:
            try:
                json_data = handler(json_data)
            except Exception as e:
                logging.warning(
                    f"[ERROR] An error occurred during the on_workflow_handler processing"
                )
                logging.warning(traceback.format_exc())

        return json_data
