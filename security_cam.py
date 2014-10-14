import datetime
import os
import time

from SimpleCV import Camera
import RPi.GPIO as GPIO

def get_file_name(extension='png'):
    dt = datetime.datetime.now().strftime("%Y-%m-%d_%H.%M.%S")
    return os.path.join("pictures", 'sc-'+dt+'.'+extension)

cam_size = {'width': 640, 'height': 480}
vid_fps = 25

sensorPin = 7

GPIO.setmode(GPIO.BOARD)
GPIO.setup(sensorPin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

prevState = False
currState = False

print("Initializing camera")
cam = Camera(0, cam_size)
r = g = b = 0
while r + g + b < 0.01:
    img = cam.getImage()
    r, g, b = img[img.width/2, img.height/2]
    print("r: {} g: {} b: {}".format(r,g,b))
    time.sleep(1)

while True:
    currState = GPIO.input(sensorPin)
    time.sleep(.1)
    if currState:  # True if movement, False if no movement
        # Save still image
        file_name = get_file_name('png')
        print("Movement detected. Saving image {}".format(file_name))
        img = cam.getImage().save(file_name)

        # Save video
        file_name = get_file_name('avi')
        print("Recording video {}".format(file_name))
        vid = VideoStream(file_name, fps=vid_fps)
        for frame in range(0, vid_fps * 10):
            img = cam.getImage()
            vid.writeFrame(img)
            time.sleep(1.0/vid_fps)
    time.sleep(5)

