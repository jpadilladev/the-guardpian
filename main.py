from picamera import PiCamera
from time import sleep
import RPi.GPIO as GPIO

camera = PiCamera()

GPIO.setmode(GPIO.BCM)
GPIO.setup(4, GPIO.IN)

try:
    sleep(2)
    while True:
        if GPIO.input(4):
            print("Motion detected!")
            #camera.start_preview(alpha=200)
            sleep(5)
            camera.capture("/home/pi/Desktop/image.jpg")
            sleep(1)
            #camera.stop_preview()
        sleep(0.1)
        
except:
    GPIO.cleanup()