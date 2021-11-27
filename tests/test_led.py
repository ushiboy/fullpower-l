from typing import List, Tuple

from fpl._io import IOInterface
from fpl._led import LED


class MockIO(IOInterface):

    def __init__(self):
        self.setup_out_channels: List[int] = []
        self.output_channel_histories: List[Tuple[int, int]] = []

    def initialize(self) -> None:
        raise NotImplementedError

    def setup_out(self, channel: int) -> None:
        self.setup_out_channels.append(channel)

    def output_high(self, channel: int) -> None:
        self.output_channel_histories.append((channel, 1))

    def output_low(self, channel: int) -> None:
        self.output_channel_histories.append((channel, 0))

    def finalize(self) -> None:
        raise NotImplementedError


def test_turn_on():
    channel = 17
    io = MockIO()
    LED(channel, io).turn_on()
    assert io.setup_out_channels == [channel]
    assert io.output_channel_histories == [(channel, 1)]


def test_turn_off():
    channel = 17
    io = MockIO()
    LED(channel, io).turn_off()
    assert io.setup_out_channels == [channel]
    assert io.output_channel_histories == [(channel, 0)]
