#!/usr/bin/env python
import os

from utils import PreparedCamera


# Settings
cam_size = {'width': 1280, 'height': 720}
file_name = os.path.join("pictures", "still_image.png")

cam = PreparedCamera(0, cam_size, debug=True)

img = cam.getImage()
img.save(file_name)
