import asyncio
import server
import nodes
import logging
import os
import time
import execution
import threading
import shutil

logging.basicConfig(
    level=logging.DEBUG, format="%(asctime)s [%(levelname)s]  %(message)s"
)


async def run(server, address="", port=4047, verbose=True, call_on_start=None):
    await asyncio.gather(
        server.start(address, port, verbose, call_on_start), server.publish_loop()
    )


def clean_pycache(directory):
    # Walk through the directory
    for root, dirs, files in os.walk(directory):
        # Check if __pycache__ is in the directories
        if "__pycache__" in dirs:
            pycache_path = os.path.join(root, "__pycache__")
            try:
                shutil.rmtree(pycache_path)  # Remove the directory
                # print(f"Deleted: {pycache_path}")
            except Exception as e:
                logging.ERROR(f"Failed to delete {pycache_path}: {e}")


def workflow_worker(q, server):
    e = execution.WorkflowExecutor(server)

    while True:
        timeout = 1000.0

        queue_item = q.get(timeout=timeout)
        if queue_item is not None:
            item, item_id = queue_item
            execution_start_time = time.perf_counter()
            prompt_id = item[1]
            server.last_prompt_id = prompt_id

            e.execute(item[2], prompt_id, item[3], item[4])
            q.task_done(
                item_id,
                e.history_result,
                status=execution.WorkflowQueue.ExecutionStatus(
                    status_str="success" if e.success else "error",
                    completed=e.success,
                    messages=e.status_messages,
                ),
            )
            if server.client_id is not None:
                server.send_sync(
                    "executing",
                    {"node": None, "prompt_id": prompt_id},
                    server.client_id,
                )

            current_time = time.perf_counter()
            execution_time = current_time - execution_start_time
            logging.info("Workflow executed in {:.2f} seconds".format(execution_time))


if __name__ == "__main__":
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)

    server = server.WorkflowServer(loop)
    workflow_executor = execution.WorkflowQueue(server)

    nodes.init_external_custom_nodes()
    server.add_routes()

    threading.Thread(
        target=workflow_worker,
        daemon=True,
        args=(
            workflow_executor,
            server,
        ),
    ).start()

    def startup_server(scheme, address, port):
        import webbrowser

        if os.name == "nt" and address == "0.0.0.0":
            address = "127.0.0.1"
        # webbrowser.open(f"{scheme}://{address}:{port}")

    call_on_start = startup_server

    try:
        loop.run_until_complete(server.setup())
        loop.run_until_complete(
            run(
                server,
                address="127.0.0.1",
                port=4047,
                verbose=True,
                call_on_start=call_on_start,
            )
        )
    except KeyboardInterrupt:
        logging.info("Stopped server")
        clean_pycache(".")
