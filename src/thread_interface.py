from threading import Thread
from src import app


class InterfaceThread(Thread):
    def __init__(self, thread_id, name):
        Thread.__init__(self)
        self.threadID = thread_id
        self.name = name

    def run(self) -> None:
        app.run(host='0.0.0.0', port=80)
