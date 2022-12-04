import cv2 as cv

def _load_image(arg):
    if isinstance(arg, str):
        return cv.imread(arg)
    return arg

def get_location(subimage, image):
    pass

def extract_images(image):
    image = _load_image(image)
    imgray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    ret, thresh = cv.threshold(imgray, 127, 255, 0)
    contours, hierarchy = cv.findContours(thresh, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
