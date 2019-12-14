import sys
import datetime
import logging as log
from time import sleep

PIN_NUMBER = 4

class GuardpianService:
    def __init__(self, base_path, camera, gpio, email_sender):
        self.base_path = base_path
        self.camera = camera
        self.gpio = gpio
        self.email_sender = email_sender

    def start(self):
        log.info('Started!')
        try:
            self.__capture_and_send('start.jpg', 'The Guardpian was started.')
            
            # Add a listener for motion events
            self.gpio.add_event_detect(PIN_NUMBER, self.__event_detect_callback)

            while True:
                sleep(100)
                
        except KeyboardInterrupt:
            log.info("Quit")
            pass
        except Exception as e: 
            log.error("Not controlled error happened: " + str(e))
            pass
        finally:
            log.info("Cleaning gpio and shutting down...")
            self.gpio.cleanup()
            self.camera.close()
            sys.exit("Shutdown.")
            
    def __event_detect_callback(self, pin):
        log.info("Motion detected!")
        self.__capture_and_send('motion.jpg', 'The Guardpian detected some movement!')


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
