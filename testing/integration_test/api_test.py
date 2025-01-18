import websocket
import requests
import uuid
import json
from typing import Dict
import pytest
import shlex
import subprocess
from time import sleep


class RunResult:
    def __init__(self, workflow_id: str):
        self.outputs: Dict[str, Dict] = {}
        self.runs: Dict[str, bool] = {}
        self.workflow_id: str = workflow_id

    def get_output(self, node_id):
        return self.outputs.get(node_id, None)

    def did_run(self, node_id):
        return self.runs.get(node_id, False)

    def get_images(self, node_id):
        output = self.get_output(node_id)
        if output is None:
            return []
        return output.get("image_objects", [])

    def get_workflow_id(self):
        return self.workflow_id


class FBPClient:
    def __init__(self):
        self.client_id = "test-client"

    def ws_connect(self, address, port):
        ws = websocket.WebSocket()
        self.url = f"{address}:{port}"
        ws.connect(f"ws://{self.url}/ws?clientId={self.client_id}")
        self.ws = ws

    def get_history(self, workflow_id):
        r = requests.get(f"http://{self.url}/history/{workflow_id}")
        return r.json()

    def stop_workflow(self):
        requests.post(f"http://{self.url}/interrupt")

    def send_workflow(self, workflow: dict):
        req_body = workflow
        req_body["client_id"] = self.client_id
        r = requests.post(f"http://{self.url}/workflow", json=req_body)

        if r.status_code != 200:
            raise Exception(r.json())

        return r.json()

    def execute(self, workflow: dict, forceInterrupt=False):
        workflow_id = self.send_workflow(workflow)["workflow_id"]

        result = RunResult(workflow_id)

        if forceInterrupt:
            sleep(3)
            self.stop_workflow()

        while True:
            out = self.ws.recv()
            if isinstance(out, str):
                message = json.loads(out)
                if message["type"] == "executing":
                    data = message["data"]
                    if data["workflow_id"] != workflow_id:
                        continue
                    if data["node"] is None:
                        break
                    result.runs[data["node"]] = True
                elif message["type"] == "execution_error":
                    raise Exception(message["data"])
                elif message["type"] == "execution_cached":
                    pass

        history = self.get_history(workflow_id)[workflow_id]
        for node_id in history["outputs"]:
            node_output = history["outputs"][node_id]
            result.outputs[node_id] = node_output

        return result


@pytest.mark.execution
class TestWorkflowExecution:
    @pytest.fixture(scope="class", autouse=True)
    def _run_program(self):
        command = "python main.py"
        p = subprocess.Popen(shlex.split(command))
        yield
        p.kill()

    def start_ws_client(self):
        client = FBPClient()

        number_of_tries = 10
        for i in range(number_of_tries):
            sleep(5)
            try:
                client.ws_connect("127.0.0.1", 4047)
            except ConnectionRefusedError as e:
                print(e)
                print(f"({i+1}/{number_of_tries}) Retrying...")
            else:
                break

        return client

    @pytest.fixture(scope="class", autouse=True)
    def shared_client(self, _run_program):
        client = self.start_ws_client()
        yield client
        del client

    @pytest.fixture
    def client(self, shared_client, request):
        yield shared_client

    def test_normal_workflow(self, client: FBPClient):
        with open(
            "./testing/integration_test/workflows/normal_workflow_test.json"
        ) as fp:
            workflow = json.load(fp)

        result = client.execute(workflow)

        output = result.get_output("10")

        assert output["text"] == [["0.0"]]

    def test_invalid_workflow(self, client: FBPClient):
        with open(
            "./testing/integration_test/workflows/invalid_workflow_test.json"
        ) as fp:
            workflow = json.load(fp)

        try:
            result = client.execute(workflow)
        except Exception as e:
            assert e.args[0]["error"]["type"] == "workflow_outputs_failed_validation"

            k = ["error", "node_errors"]
            assert k[0] in e.args[0].keys()
            assert k[1] in e.args[0].keys()

    def test_error_workflow(self, client: FBPClient):
        with open(
            "./testing/integration_test/workflows/error_workflow_test.json"
        ) as fp:
            workflow = json.load(fp)

        try:
            result = client.execute(workflow)
        except Exception as e:

            lst = [
                "workflow_id",
                "node_id",
                "node_type",
                "executed",
                "exception_message",
                "exception_type",
                "traceback",
                "current_inputs",
                "current_outputs",
                "timestamp",
            ]

            ex = e.args[0]

            for i in lst:
                assert i in ex.keys()

    def test_interrupt_workflow(self, client: FBPClient):
        with open(
            "./testing/integration_test/workflows/interrupt_workflow_test.json"
        ) as fp:
            workflow = json.load(fp)

        try:
            result = client.execute(workflow, forceInterrupt=True)

        except Exception as e:

            lst = [
                "workflow_id",
                "node_id",
                "node_type",
                "executed",
                "exception_message",
                "exception_type",
                "traceback",
                "current_inputs",
                "current_outputs",
            ]

            ex = e.args[0]

            for i in lst:
                assert i in ex.keys()

            assert ex["exception_type"] == "InterruptedError"
