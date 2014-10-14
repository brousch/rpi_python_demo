import datetime
import os
import time

from SimpleCV import Camera
import RPi.GPIO as GPIO

def get_file_name():
    dt = datetime.datetime.now().strftime("%Y-%m-%d_%H.%M.%S")
    return os.path.join("pictures", dt+".jpg")

sensorPin = 7

GPIO.setmode(GPIO.BOARD)
GPIO.setup(sensorPin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

prevState = False
currState = False

cam_size = {'width': 1280, 'height':720}
cam = Camera(0, cam_size)

while True:
    currState = GPIO.input(sensorPin)
    time.sleep(.1)
    if currState:  # True if movement, False if no movement
        file_name = get_file_name()
        print("Movement detected. Taking photo {}".format(file_name))
        img = cam.getImage()
        img.save(file_name)
        time.sleep(5)

