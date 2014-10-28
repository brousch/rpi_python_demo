# Utilities for working with SimpleCV and webcams
from time import sleep
from SimpleCV import Camera


class PreparedCamera(Camera):
    def __init__(self, *args, **kwargs):
        # Pull out debug kwarg before passing to Camera
        try:
            self.debug = kwargs['debug']
            del kwargs['debug']
            print("Initializing camera")
        except KeyError:
            self.debug = False
        Camera.__init__(self, *args, **kwargs)

        while not self.camera_is_ready():
            sleep(1)
        if self.debug:
            print("Camera is ready")

    def camera_is_ready(self):
        ''' Returns True if the camera gets a non-black image.
        '''
        img = self.getImage()
        r, g, b = img[img.width/2, img.height/2]
        if self.debug:
            print("r:{} g:{} b:{}".format(r,g,b))
        if r + g + b > 0:
            return True
        return False