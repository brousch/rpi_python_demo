#!/usr/bin/env python
import os
from time import sleep

from SimpleCV import VideoStream

from utils import PreparedCamera


# Settings
cam_size = {'width': 320, 'height': 240}
vid_fps = 15
file_name = os.path.join('pictures', 'video.avi')

cam = PreparedCamera(0, cam_size, debug=True)

print("Recording video")
vid = VideoStream(file_name, fps=vid_fps)
for frame in range(0, vid_fps * 10):
    img = cam.getImage()
    vid.writeFrame(img)
    sleep(1.0/vid_fps)
