import os
import time

from SimpleCV import Camera

from utils import camera_is_ready


cam_size = {'width': 1280, 'height': 720}
file_name = os.path.join("pictures", "still_image.png")

print("Initializing camera")
cam = Camera(0, cam_size)
while not camera_is_ready(cam, debug=True):
    time.sleep(1)

img = cam.getImage()
img.save(file_name)
