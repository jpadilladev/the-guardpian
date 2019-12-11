from time import sleep
from picamera import PiCamera
from fractions import Fraction
import logging as log


class Camera:
    def __init__(self, debug):
        self.debug = debug
        if not self.debug:
            self.camera = PiCamera(resolution=(1280, 720))
            self.camera.led = False

    def capture(self, path):
        if not self.debug:
            self.camera.start_preview(alpha=200)
            sleep(2)  # warm up the camera
            self.camera.capture(path)
            self.camera.stop_preview()
        log.info('Captured on' + path)
