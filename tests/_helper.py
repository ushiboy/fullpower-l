from typing import List, Tuple

from fpl._io import IOInterface


class MockIO(IOInterface):

    def __init__(self):
        self.setup_out_channels: List[int] = []
        self.output_channel_histories: List[Tuple[int, int]] = []
        self.finalized = False

    def initialize(self) -> None:
        raise NotImplementedError

    def setup_out(self, channel: int) -> None:
        self.setup_out_channels.append(channel)

    def output_high(self, channel: int) -> None:
        self.output_channel_histories.append((channel, 1))

    def output_low(self, channel: int) -> None:
        self.output_channel_histories.append((channel, 0))

    def finalize(self) -> None:
        self.finalized = True
