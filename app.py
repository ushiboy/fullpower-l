import signal
from fpl import Application, raise_terminated

if __name__ == '__main__':
    signal.signal(signal.SIGTERM, raise_terminated)
    channel = 17
    Application.create(channel).run()
