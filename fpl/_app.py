from __future__ import annotations

import time

from ._exception import TerminatedException
from ._gpio import GPIO
from ._io import IOInterface
from ._led import LED


class Application:

    def __init__(self, io: IOInterface, led_channel: int):
        self._io = io
        self._led_channel = led_channel
        self._led_status = False  # On: True, Off: False

    def run(self) -> None:
        try:
            led = LED(self._led_channel, self._io)
            while True:
                self._led_status = app_process(led, self._led_status)
                time.sleep(1)
        except (KeyboardInterrupt, TerminatedException):
            pass  # ignore
        finally:
            self._io.finalize()

    @classmethod
    def create(cls, led_channel: int) -> Application:
        io = GPIO.create()
        return cls(io, led_channel)


def app_process(led: LED, led_status: bool) -> bool:
    if led_status:
        led.turn_off()
    else:
        led.turn_on()
    return not led_status
