from SimpleCV import Camera, JpegStreamer


# Settings
cam_size = {'width': 640, 'height':480}
framerate = 15 # frames per second
stream_host = 'localhost'
stream_port = 8080
stream_length = 60 # seconds

cam = Camera(0, cam_size)
stream = JpegStreamer(hostandport=(stream_host, stream_port), 
                      st=1.0/framerate)

print("Now streaming at {}".format(stream.url()))
for frames in range(0, framerate*stream_length):
    cam.getImage().save(stream)
