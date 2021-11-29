class IOInterface:

    def initialize(self) -> None:
        raise NotImplementedError

    def setup_out(self, channel: int) -> None:
        raise NotImplementedError

    def output_high(self, channel: int) -> None:
        raise NotImplementedError

    def output_low(self, channel: int) -> None:
        raise NotImplementedError

    def finalize(self) -> None:
        raise NotImplementedError
