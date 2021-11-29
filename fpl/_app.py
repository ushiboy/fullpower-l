from __future__ import annotations

import time
from typing import Callable

from ._exception import TerminatedException
from ._gpio import GPIO
from ._io import IOInterface
from ._led import LED

AppProc = Callable[[LED, bool], bool]


def app_process(led: LED, led_status: bool) -> bool:
    if led_status:
        led.turn_off()
    else:
        led.turn_on()
    return not led_status


class Application:

    def __init__(self, io: IOInterface, led_channel: int, app_proc: AppProc = app_process, wait_sec: int = 1):
        self._io = io
        self._led_channel = led_channel
        self._app_process = app_proc
        self._wait_sec = wait_sec

    def run(self) -> None:
        led_status = False  # On: True, Off: False
        try:
            led = LED(self._led_channel, self._io)
            while True:
                led_status = self._app_process(led, led_status)
                time.sleep(self._wait_sec)
        except (KeyboardInterrupt, TerminatedException):
            pass  # ignore
        finally:
            self._io.finalize()

    @classmethod
    def create(cls, led_channel: int) -> Application:
        io = GPIO.create()
        return cls(io, led_channel)
