# Utilities for working with SimpleCV and webcams

def camera_is_ready(cam, debug=False):
    ''' Returns True if the camera creates a non-black image.
    '''
    img = cam.getImage()
    r, g, b = img[img.width/2, img.height/2]
    if debug:
        print("r: {} g: {} b: {}".format(r,g,b))
    if r + g + b > 0:
        return True
    return False
