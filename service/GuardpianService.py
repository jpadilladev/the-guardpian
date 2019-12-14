import logging as log
import sys
from time import sleep


class GuardpianService:
    def __init__(self, base_path, camera, gpio, email_sender, ifttt_enabled, ifttt_client):
        self.base_path = base_path
        self.camera = camera
        self.gpio = gpio
        self.email_sender = email_sender
        self.ifttt_enabled = ifttt_enabled
        self.ifttt_client = ifttt_client
        self.is_ifttt_on = False  # To avoid unnecessary IFTTT calls

    def start(self):
        try:
            self.__capture_on_start()

            # Add listeners for GPIO events
            self.gpio.add_event_detect_rising(self.__event_detect_callback_on)
            self.gpio.add_event_detect_falling(self.__event_detect_callback_off)

            # Loop forever
            while True:
                sleep(100)

        except KeyboardInterrupt:
            log.info("Quit")
            pass
        except Exception as e:
            log.error("Not controlled error happened: " + str(e))
            self.__send(image_full_path=None,
                        content="Some uncontrolled Error happened... Shutting down. Error: " + str(e))
            pass
        finally:
            log.info("Cleaning GPIO and shutting down...")
            self.gpio.cleanup()
            self.camera.close()
            sys.exit("Shutdown.")

    def __capture_on_start(self):
        log.info('Started The Guardpian!')
        if self.ifttt_enabled:
            self.__send_ifttt_event_on()
        self.__capture_and_send('start.jpg', 'The Guardpian was started.')
        if self.ifttt_enabled:
            self.__send_ifttt_event_off()

    def __capture_and_send(self, image_name, content):
        try:
            image_full_path = self.base_path + image_name
            self.camera.capture(image_full_path)
            self.__send(image_full_path, content)
        except Exception as e:
            log.error("Cannot capture... " + str(e))

    def __send(self, image_full_path, content):
        try:
            self.email_sender.send(content, image_full_path)
        except Exception as e:
            log.error("Cannot send email... " + str(e))

    def __event_detect_callback_on(self, pin):
        log.info("Motion detected!")
        if self.ifttt_enabled:
            self.__send_ifttt_event_on()
        self.__capture_and_send('motion.jpg', 'The Guardpian detected some motion!')

    def __event_detect_callback_off(self, pin):
        log.info("Motion off.")
        if self.ifttt_enabled:
            self.__send_ifttt_event_off()

    def __send_ifttt_event_on(self):
        try:
            self.ifttt_client.send_event_on()
            self.is_ifttt_on = True
            sleep(1.5)
        except Exception as e:
            log.error("Cannot send IFTTT event ON ... " + str(e))

    def __send_ifttt_event_off(self):
        try:
            if self.is_ifttt_on:
                sleep(5)
                self.ifttt_client.send_event_off()
                self.is_ifttt_on = False
        except Exception as e:
            log.error("Cannot send IFTTT event Off ... " + str(e))
