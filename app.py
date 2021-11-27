import time
from fpl import GPIO, LED

channel = 17
io = GPIO.create()
led = LED(channel, io)

try:
    while True:
        led.turn_on()
        time.sleep(1)
        led.turn_off()
        time.sleep(1)
finally:
    io.finalize()
