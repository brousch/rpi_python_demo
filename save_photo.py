import os
import time
from SimpleCV import Camera

cam_size = {'width': 1280, 'height': 720}
file_name = os.path.join("pictures", "still_image.png")

cam = Camera(0, cam_size)
r = g = b = 0
while r + g + b < 0.01:
    img = cam.getImage()
    r, g, b = img[img.width/2, img.height/2]
    print("r: {} g: {} b: {}".format(r,g,b))
    time.sleep(1)
img.save(file_name)
