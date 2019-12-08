from random import randint

import RPi.GPIO as GPIO


class Gpio:
    def __init__(self, debug):
        self.debug = debug
        if not self.debug:
            GPIO.setmode(GPIO.BCM)
            GPIO.setup(4, GPIO.IN)

    def input(self, pin):
        if self.debug:
            return randint(0, 10) < 3
        else:
            return GPIO.input(pin)

    def cleanup(self):
        if not self.debug:
            GPIO.cleanup()
