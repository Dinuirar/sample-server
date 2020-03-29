from threading import Thread
from src.controller import Controller


class ControllerThread(Thread):
    def __init__(self, thread_id, name):
        Thread.__init__(self)
        self.threadID = thread_id
        self.name = name
        self.controller = Controller()

    def run(self) -> None:
        self.controller.run()
