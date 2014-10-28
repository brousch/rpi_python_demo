import datetime
import os
from time import sleep

from SimpleCV import Camera

try:
    import RPi.GPIO as GPIO
except:
    print("RPi.GPIO is not installed or could not be found.")

from utils import camera_is_ready


# Settings
cam_size = {'width': 1280, 'height':720}
sensorPin = 7


def get_file_name():
    dt = datetime.datetime.now().strftime("%Y-%m-%d_%H.%M.%S")
    return os.path.join("pictures", dt+".jpg")


GPIO.setmode(GPIO.BOARD)
GPIO.setup(sensorPin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

prevState = False
currState = False

print("Initializing camera.")
cam = Camera(0, cam_size)
while not camera_is_ready(cam, debug=True):
    sleep(1)
print("Camera is ready.")

while True:
    currState = GPIO.input(sensorPin)
    sleep(.1)
    if currState:  # True if movement, False if no movement
        file_name = get_file_name()
        print("Movement detected. Taking photo {}".format(file_name))
        img = cam.getImage()
        img.save(file_name)
        sleep(5)
