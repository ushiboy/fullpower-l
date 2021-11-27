from fpl._app import app_process
from fpl._led import LED

from ._helper import MockIO


def test_app_process():
    channel = 17
    io = MockIO()
    led = LED(channel, io)

    assert not app_process(led, True)
    assert io.output_channel_histories == [(channel, 0)]

    assert app_process(led, False)
    assert io.output_channel_histories == [(channel, 0), (channel, 1)]
