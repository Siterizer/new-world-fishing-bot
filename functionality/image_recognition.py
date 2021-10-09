from numpy import array
import cv2 as cv
from PIL import ImageGrab
from utils.global_variables import WAITING_FOR_FISH, FISH_NOTICED

NOTHING = cv.imread(WAITING_FOR_FISH)
NOTICE = cv.imread(FISH_NOTICED)
REEL_COLOR = (4, 227, 162)
WAIT_COLOR_BROWN = (230, 110, 22)
WAIT_COLOR_RED = (109, 18, 21)
COLOR_WAGES = 7

def image_recognition_result(x, y, width, height):
    region=(x, y, x + width, y + height)
    img = ImageGrab.grab(bbox = region)
    img_cv = cv.cvtColor(array(img), cv.COLOR_RGB2BGR)
    res = cv.matchTemplate(img_cv, NOTICE, eval('cv.TM_CCOEFF_NORMED'))
    if((res >= 0.7).any()):
        return '1'
    res = cv.matchTemplate(img_cv, NOTHING, eval('cv.TM_CCOEFF_NORMED'))
    if((res >= 0.7).any()):
        return '0'

    for i in range(width):
        for j in range(height):
            color = img.getpixel((i, j))
            if pixel_match(color, REEL_COLOR):
                return '2'
            if pixel_match(color, WAIT_COLOR_BROWN):
                return '3'
            if pixel_match(color, WAIT_COLOR_RED):
                return '4'
    return '5'

def pixel_match(color, matcher):
    for i in range (0,3):
        if not((matcher[i] - COLOR_WAGES) <= color[i] <= (matcher[i] + COLOR_WAGES)):
            return False
    return True
