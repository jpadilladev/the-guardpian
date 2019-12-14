import logging as log

import RPi.GPIO as GPIO


class Gpio:
    def __init__(self, debug, pin=4):
        self.debug = debug
        self.pin = pin
        if not self.debug:
            GPIO.setmode(GPIO.BCM)
            GPIO.setup(self.pin, GPIO.IN)

    def add_event_detect_rising(self, callback):
        if not self.debug:
            GPIO.add_event_detect(self.pin, GPIO.RISING, callback=callback, bouncetime=200)
        log.info("Added event detect to GPIO Rising" + str(self.pin))

    def add_event_detect_falling(self, callback):
        if not self.debug:
            GPIO.add_event_detect(self.pin, GPIO.FALLING, callback=callback, bouncetime=200)
        log.info("Added event detect to GPIO Falling" + str(self.pin))

    def remove_event_detect(self):
        if not self.debug:
            GPIO.remove_event_detect(self.pin)
        log.info("Removed event detect to GPIO " + str(self.pin))

    def cleanup(self):
        if not self.debug:
            GPIO.cleanup()
