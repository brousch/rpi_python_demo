import os
import time

from SimpleCV import Camera, VideoStream

from utils import camera_is_ready


# Settings
cam_size = {'width': 640, 'height': 480}
vid_fps = 25
file_name = os.path.join('pictures', 'video.avi')

print("Initializing camera.")
cam = Camera(0, cam_size)
while not camera_is_ready(cam, debug=True):
    time.sleep(1)
print("Camera is ready.")

print("Recording video")
vid = VideoStream(file_name, fps=vid_fps)
for frame in range(0, vid_fps * 10):
    img = cam.getImage()
    vid.writeFrame(img)
    time.sleep(1.0/vid_fps)
