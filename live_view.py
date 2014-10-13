from SimpleCV import Camera

cam_size = {'width': 640, 'height':480}

cam = Camera(0, cam_size)
cam.live()
