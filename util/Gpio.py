import logging

import RPi.GPIO as GPIO


log = logging.getLogger(__name__)

class Gpio:
    def __init__(self, debug, pin=4):
        self.debug = debug
        self.pin = pin
        if not self.debug:
            GPIO.setmode(GPIO.BCM)
            GPIO.setup(self.pin, GPIO.IN)

    def add_event_detect(self, callback):
        if not self.debug:
            GPIO.add_event_detect(self.pin, GPIO.BOTH, callback=callback, bouncetime=200)
        log.info("Added event detect to GPIO BOTH on pin " + str(self.pin))

    def remove_event_detect(self):
        if not self.debug:
            GPIO.remove_event_detect(self.pin)
        log.info("Removed event detect to GPIO pin " + str(self.pin))
        
    def input(self):
        if not self.debug:
            return GPIO.input(self.pin)
        else:
            return True

    def cleanup(self):
        if not self.debug:
            GPIO.cleanup()
