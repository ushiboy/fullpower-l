import time
from threading import Thread

from fpl._app import Application, app_process
from fpl._exception import TerminatedException
from fpl._led import LED

from ._helper import MockIO


def test_app_run():
    channel = 17
    io = MockIO()
    state = {"count": 0}

    def wrap(led: LED, led_status: bool) -> bool:
        state["count"] += 1
        if state["count"] > 3:
            raise TerminatedException
        return app_process(led, led_status)

    def t():
        Application(io, channel, wrap, 0.1).run()

    th = Thread(target=t, daemon=True)
    th.start()
    time.sleep(0.5)
    th.join(1)
    assert io.output_channel_histories == [
        (channel, 1), (channel, 0), (channel, 1)]
    assert io.finalized


def test_app_process():
    channel = 17
    io = MockIO()
    led = LED(channel, io)

    assert not app_process(led, True)
    assert io.output_channel_histories == [(channel, 0)]

    assert app_process(led, False)
    assert io.output_channel_histories == [(channel, 0), (channel, 1)]
