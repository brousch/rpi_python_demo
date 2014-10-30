import datetime
import os
from time import sleep

from SimpleCV import VideoStream

from utils import PreparedCamera


# Settings
cam_size = {'width': 320, 'height': 240}
vid_fps = 15
vid_length = 10 # seconds


def get_file_name(extension='png'):
    dt = datetime.datetime.now().strftime("%Y-%m-%d_%H%M%S")
    return os.path.join("pictures", 'sc-'+dt+'.'+extension)


cam = PreparedCamera(0, cam_size, debug=True)

sleep(1)
# Save still image
file_name = get_file_name('png')
print("Movement detected. Saving image {}".format(file_name))
img = cam.getImage().save(file_name)

sleep(1)
# Save video
file_name = get_file_name('avi')
print("Recording video {}".format(file_name))
vid = VideoStream(file_name, fps=vid_fps)
for frame in range(0, int(vid_fps * vid_length)):
    img = cam.getImage()
    vid.writeFrame(img)
    sleep(1.0/vid_fps)
