from fpl._led import LED

from ._helper import MockIO


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
