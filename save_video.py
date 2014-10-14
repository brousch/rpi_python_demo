import os
import time
from SimpleCV import Camera, VideoStream

cam_size = {'width': 640, 'height': 480}
vid_fps = 25
file_name = os.path.join("pictures", "video.mp4")

print("Initializing camera")
cam = Camera(0, cam_size)
r = g = b = 0
while r + g + b < 0.01:
    img = cam.getImage()
    r, g, b = img[img.width/2, img.height/2]
    print("r: {} g: {} b: {}".format(r,g,b))
    time.sleep(1)

print("Recording video")
vid = VideoStream(file_name, fps=vid_fps)
for frame in range(0, vid_fps * 10):
    cam.getImage().save(vid)
    time.sleep(1.0/vid_fps)

