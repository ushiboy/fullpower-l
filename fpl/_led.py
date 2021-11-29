from ._io import IOInterface


class LED:

    def __init__(self, channel: int, io: IOInterface):
        self._channel = channel
        self._io = io
        self._io.setup_out(channel)

    def turn_on(self) -> None:
        self._io.output_high(self._channel)

    def turn_off(self) -> None:
        self._io.output_low(self._channel)
