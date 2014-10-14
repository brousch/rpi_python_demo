import os
import time

from SimpleCV import Camera, ImageSet

from utils import camera_is_ready

cam_size = {'width': 640, 'height': 480}
gif_interval = 0.5 # Seconds between frames
gif_length = 10 # Length in seconds
file_name = os.path.join('pictures', 'ani.gif')

print("Initializing camera")
cam = Camera(0, cam_size)
while not camera_is_ready(cam, debug=True):
    time.sleep(1)

print("Recording images")
img_set = ImageSet()
for frame in range(0, int(gif_length * gif_interval)):
    img = cam.getImage()
    img_set.append(img)
    time.sleep(1.0/gif_interval)
img_set.save(destination=file_name, dt=gif_interval)
