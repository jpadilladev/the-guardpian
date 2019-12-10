import sys
from time import sleep


class GuardpianService:
    def __init__(self, camera, gpio):
        self.camera = camera
        self.gpio = gpio

    def start(self):
        print('Start!')
        self.camera.capture("/home/pi/Desktop/start_capture.jpg")
        try:
            sleep(2)
            while True:
                print('loop')
                if self.gpio.input(4):
                    print("Motion detected!")
                    try:
                        self.camera.capture("/home/pi/Desktop/motion_capture.jpg")
                        sleep(1)
                    except:
                        print("Cannot capture.")
                sleep(0.1)
        except:
            print("Error occurred, cleaning gpio and shutting down...")
            self.gpio.cleanup()
            sys.exit("Shutdown.")
