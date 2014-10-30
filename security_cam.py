import datetime
import os
from time import sleep

from SimpleCV import VideoStream

try:
    import RPi.GPIO as GPIO
except:
    print("RPi.GPIO is not installed or could not be found.")

from utils import PreparedCamera


# Settings
cam_size = {'width': 320, 'height': 240}
vid_fps = 15
vid_length = 10 # seconds
sensorPin = 7


def get_file_name(extension='png'):
    dt = datetime.datetime.now().strftime("%Y-%m-%d_%H%M%S")
    return os.path.join("pictures", 'sc-'+dt+'.'+extension)


GPIO.setmode(GPIO.BOARD)
GPIO.setup(sensorPin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

prevState = False
currState = False

cam = PreparedCamera(0, cam_size, debug=True)

while True:
    currState = GPIO.input(sensorPin)
    sleep(.1)
    if currState:  # True if movement, False if no movement
        # Save still image
        file_name = get_file_name('png')
        print("Movement detected. Saving image {}".format(file_name))
        img = cam.getImage().save(file_name)

        # Save video
        file_name = get_file_name('avi')
        print("Recording video {}".format(file_name))
        vid = VideoStream(file_name, fps=vid_fps)
        for frame in range(0, int(vid_fps * vid_length)):
            img = cam.getImage()
            vid.writeFrame(img)
            sleep(1.0/vid_fps)
    sleep(5)
