import sys
from time import sleep


class GuardpianService:
    def __init__(self, camera, gpio):
        self.camera = camera
        self.gpio = gpio

    def start(self):
        print('Start!')
        try:
            sleep(2)
            while True:
                print('loop')
                if self.gpio.input(4):
                    print("Motion detected!")
                    try:
                        # camera.start_preview(alpha=200)
                        self.camera.capture("/home/pi/Desktop/image.jpg")
                        sleep(1)
                    except:
                        print("Cannot capture.")
                    # camera.stop_preview()
                sleep(0.1)
        except:
            print("Error occurred, cleaning gpio and shutting down...")
            self.gpio.cleanup()
            sys.exit("Shutdown.")
