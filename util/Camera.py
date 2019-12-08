from time import sleep
from picamera import PiCamera


class Camera:
    def __init__(self, debug):
        self.debug = debug
        if not self.debug:
            self.camera = PiCamera()

    def capture(self, path):
        sleep(5)
        if not self.debug:
            self.camera.capture(path)
        print('Captured on' + path)
