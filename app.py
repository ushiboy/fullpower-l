import time
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

channel = 17

GPIO.setup(channel, GPIO.OUT)

try:
    while True:
        GPIO.output(channel, GPIO.HIGH)
        time.sleep(1)
        GPIO.output(channel, GPIO.LOW)
        time.sleep(1)
finally:
    GPIO.output(channel, GPIO.LOW)
    GPIO.cleanup()
