from src.thread_interface import InterfaceThread
from src.thread_controller import ControllerThread
import subprocess


def main():
    subprocess.Popen("net start MySQL82", shell=True, stdout=subprocess.PIPE)

    interface = InterfaceThread(1, "interface")
    controller = ControllerThread(2, "controller")

    interface.start()
    controller.start()

    print("closing SAMPLE server Interface-Controller app")


if __name__ == '__main__':
    main()
