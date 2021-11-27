from __future__ import annotations

try:
    import RPi.GPIO as _GPIO  # type: ignore
except RuntimeError:
    pass  # ignore

from ._io import IOInterface


class GPIO(IOInterface):

    def initialize(self) -> None:
        _GPIO.setmode(_GPIO.BCM)
        _GPIO.setwarnings(False)

    def setup_out(self, channel: int) -> None:
        _GPIO.setup(channel, _GPIO.OUT)

    def output_high(self, channel: int) -> None:
        _GPIO.output(channel, _GPIO.HIGH)

    def output_low(self, channel: int) -> None:
        _GPIO.output(channel, _GPIO.LOW)

    def finalize(self) -> None:
        _GPIO.cleanup()

    @classmethod
    def create(cls) -> GPIO:
        o = cls()
        o.initialize()
        return o
