import os
from time import sleep

from SimpleCV import ImageSet

from utils import PreparedCamera


# Settings
cam_size = {'width': 640, 'height': 480}
gif_interval = 0.5 # Seconds between frames
gif_length = 10 # Length in seconds
file_name = os.path.join('pictures', 'ani.gif')

cam = PreparedCamera(0, cam_size, debug=True)

print("Recording images")
img_set = ImageSet()
for frame in range(0, int(gif_length * gif_interval)):
    img = cam.getImage()
    img_set.append(img)
    sleep(1.0/gif_interval)
img_set.save(destination=file_name, dt=gif_interval)
