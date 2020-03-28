from src import app
import subprocess


def main():
    subprocess.Popen("net start MySQL82", shell=True, stdout=subprocess.PIPE)
    app.run(host='0.0.0.0', port=2137)


if __name__ == '__main__':
    main()
