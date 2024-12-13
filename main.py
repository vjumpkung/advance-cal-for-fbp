import asyncio
import server
import nodes
import logging
import os
import time
import execution
import threading
import shutil
from thread_manager import interrupt_completed,StoppableThread
from time import sleep

logging.basicConfig(
    level=logging.DEBUG, format="%(asctime)s [%(levelname)s]  %(message)s"
)


async def run(server, address="", port=4047, verbose=True, call_on_start=None):
    await asyncio.gather(
        server.start(address, port, verbose, call_on_start), server.publish_loop()
    )


def clean_input_directory(file_to_preserve=None):
    """
    Clean the ./input/ directory by removing all files except the specified file.

    Args:
        file_to_preserve (str, optional): Name of the file to keep in the directory.
                                          If None, no files will be preserved.

    Returns:
        tuple: (list of removed files, list of preserved files)
    """
    # Ensure the input directory exists
    input_dir = "./input/"
    if not os.path.exists(input_dir):
        print(f"Directory {input_dir} does not exist.")
        return [], []

    # Get list of all files in the directory
    all_files = os.listdir(input_dir)

    # Separate files to remove and preserve
    files_to_remove = []
    files_preserved = []

    for filename in all_files:
        file_path = os.path.join(input_dir, filename)

        # Skip if it's a directory
        if os.path.isdir(file_path):
            continue

        # Check if this is the file to preserve
        if file_to_preserve and filename == file_to_preserve:
            files_preserved.append(filename)
            continue

        # Remove the file
        try:
            os.remove(file_path)
            files_to_remove.append(filename)
            # print(f"Removed: {filename}")
        except Exception as e:
            logging.ERROR(f"Error removing {filename}: {e}")

    return files_to_remove, files_preserved


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


def interrupt_checker():

    while True:
        sleep(1)
        # print(interrupt_completed.is_set())
        if interrupt_completed.is_set():
            return


def workflow_worker(q, server):
    e = execution.WorkflowExecutor(server)
    while True:
        timeout = 1000.0
        queue_item = q.get(timeout=timeout)
        if queue_item is not None:
            execution_start_time = time.perf_counter()
            item, item_id = queue_item
            workflow_id = item[1]
            server.last_prompt_id = workflow_id
            try:
                executor = StoppableThread(
                    target=e.execute,
                    daemon=True,
                    args=(item[2], workflow_id, item[3], item[4]),
                )
                interrupt = threading.Thread(
                    target=interrupt_checker,
                )

                interrupt.start()
                executor.start()
                interrupt.join()
                # interrupt_completed.wait()
                # logging.debug(interrupt_completed.is_set())
                if executor.is_alive():
                    executor.kill()
                    raise InterruptedError
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
                        {"node": None, "prompt_id": workflow_id},
                        server.client_id,
                    )

                current_time = time.perf_counter()
                execution_time = current_time - execution_start_time
                
            except InterruptedError:
                logging.info("Workflow execution was interrupted")
                q.task_done(
                    item_id,
                    None,
                    status=execution.WorkflowQueue.ExecutionStatus(
                        status_str="error",
                        completed=False,
                        messages=["Execution was interrupted"],
                    ),
                )
                msg = {
                    "workflow_id": workflow_id,
                    "node_id": None,
                    "node_type": None,
                    "executed": None,
                    "exception_message": f"Workflow has been stopped by user.",
                    "exception_type": "InterruptedError",
                    "traceback": [],
                    "current_inputs": [],
                    "current_outputs": [],
                }
                current_time = time.perf_counter()
                execution_time = current_time - execution_start_time
                server.send_sync("execution_error", msg, server.client_id)
            finally:
                logging.info("Workflow executed in {:.2f} seconds".format(execution_time))
                interrupt_completed.clear()


if __name__ == "__main__":
    clean_input_directory("file_goes_here")
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
        clean_input_directory("file_goes_here")
