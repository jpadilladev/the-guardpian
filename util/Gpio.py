from random import randint

import RPi.GPIO as GPIO
import logging as log


class Gpio:
    def __init__(self, debug):
        self.debug = debug
        if not self.debug:
            GPIO.setmode(GPIO.BCM)
            GPIO.setup(4, GPIO.IN)
            
    def add_event_detect(self, pin, callback):
        if not self.debug:
            GPIO.add_event_detect(pin, GPIO.RISING, callback=callback, bouncetime=200)
        log.info("Added event detect to GPIO " + str(pin))
        
                
    def remove_event_detect(self, pin):
        if not self.debug:
            GPIO.remove_event_detect(pin)
        log.info("Removed event detect to GPIO " + str(pin))

    def cleanup(self):
        if not self.debug:
            GPIO.cleanup()
