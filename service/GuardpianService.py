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
        log.info('Start!')
        try:
            sleep(2)
            self.capture_and_send('start.jpg', 'The Guardpian was started.')
            while True:
                if self.gpio.input(4):
                    log.info("Motion detected!")
                    self.capture_and_send('motion.jpg', 'The Guardpian detected some movement!')
                    sleep(1)
                sleep(1)
        except:
            log.error("Error occurred, cleaning gpio and shutting down...")
            self.gpio.cleanup()
            sys.exit("Shutdown.")

    def capture_and_send(self, image_name, content):
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
