from threading import Thread
import subprocess
from src import app


class InterfaceThread(Thread):
    def __init__(self, thread_id, name):
        Thread.__init__(self)
        self.threadID = thread_id
        self.name = name

    def run(self) -> None:
        subprocess.Popen("net start MySQL82", shell=True, stdout=subprocess.PIPE)
        app.run(host='0.0.0.0', port=2137)
