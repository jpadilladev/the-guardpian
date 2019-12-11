import sys
import datetime
import logging as log
from time import sleep


class GuardpianService:
    def __init__(self, base_path, camera, gpio, email_sender):
        self.base_path = base_path
        self.camera = camera
        self.gpio = gpio
        self.email_sender = email_sender

    def start(self):
        log.info('Started!')
        try:
            sleep(2)
            self.__capture_and_send('start.jpg', 'The Guardpian was started.')
            activated = False
            while True:
                motion = self.gpio.input(4)
                if motion and not activated:
                    log.info("Motion detected!")
                    self.__capture_and_send('motion.jpg', 'The Guardpian detected some movement!')
                    activated = True
                elif not motion:
                    activated = False
                sleep(0.5)
        except:
            log.error("Error occurred, cleaning gpio and shutting down...")
            pass
        finally:
            self.gpio.cleanup()
            sys.exit("Shutdown.")


    def __capture_and_send(self, image_name, content):
        try:
            image_full_path = self.base_path + image_name
            self.camera.capture(image_full_path)
            self.__send(image_full_path, content)
        except:
            log.error("Cannot capture...")

    def __send(self, image_full_path, content):
        try:
            self.email_sender.send(content, image_full_path)
        except:
            log.error("Cannot send email...")
