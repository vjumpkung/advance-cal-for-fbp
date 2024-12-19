import threading
import ctypes

interrupt_completed = threading.Event()
interrupt_completed.clear()


class StoppableThread(threading.Thread):
    def __init__(self, target=None, name=None, args=(), kwargs=None, *, daemon=None):
        super().__init__(
            target=target, name=name, args=args, kwargs=kwargs, daemon=daemon
        )
        self._return = None

    def run(self):
        if self._target is not None:
            self._return = self._target(*self._args, **self._kwargs)

    def join(self, timeout=None, *args):
        super().join(timeout=timeout, *args)
        return self._return

    def start(self):
        super().start()

    def kill(self):
        if not self.is_alive():
            return

        # Get the thread ID from the ident attribute
        thread_id = self.ident
        if thread_id is None:
            raise Exception("Thread ID is None")

        res = ctypes.pythonapi.PyThreadState_SetAsyncExc(
            ctypes.c_long(thread_id), ctypes.py_object(SystemExit)
        )

        if res == 0:
            raise Exception("invalid thread id")
        elif res > 1:
            # If it returns a number greater than 1, we must undo our action to prevent issues
            ctypes.pythonapi.PyThreadState_SetAsyncExc(thread_id, 0)
        return self._return
