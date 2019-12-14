import logging

from picamera import PiCamera

log = logging.getLogger(__name__)

class Camera:
    def __init__(self, debug):
        self.debug = debug
        if not self.debug:
            self.camera = PiCamera(resolution=(1920, 1080), framerate=30)
            self.camera.led = False
            self.camera.exposure_mode = 'night'

    def capture(self, path):
        if not self.debug:
            self.camera.start_preview()
            self.camera.capture(path)
            self.camera.stop_preview()
        log.info('Captured on' + path)

    def close(self):
        if not self.debug:
            self.camera.close()
