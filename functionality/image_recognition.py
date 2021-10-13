from utils.config import dict
from numpy import array
import cv2 as cv
import numpy as np
from PIL import ImageGrab
from utils.global_variables import WAITING_FOR_FISH, FISH_NOTICED

NOTHING = cv.imread(WAITING_FOR_FISH)
NOTICE = cv.imread(FISH_NOTICED)
REEL_COLOR = dict['colors']['green']
WAIT_COLOR_BROWN = dict['colors']['brown']
WAIT_COLOR_RED = dict['colors']['red']
COLOR_WAGES = 7

def image_recognition_result(x, y, width, height):
    region=(x, y, x + width, y + height)
    img = array(ImageGrab.grab(bbox = region))
    img_cv = cv.cvtColor(img, cv.COLOR_RGB2BGR)
    res = cv.matchTemplate(img_cv, NOTICE, eval('cv.TM_CCOEFF_NORMED'))
    if((res >= 0.7).any()):
        return '1'
    res = cv.matchTemplate(img_cv, NOTHING, eval('cv.TM_CCOEFF_NORMED'))
    if((res >= 0.7).any()):
        return '0'
    
    if pixel_match(img, REEL_COLOR):     
        return '2'
    if pixel_match(img, WAIT_COLOR_BROWN):        
        return '3'
    if pixel_match(img, WAIT_COLOR_RED):                    
        return '4'           
    return '5'

def pixel_match(img, matcher):
    lower, upper = ([matcher[0] - COLOR_WAGES, matcher[1] - COLOR_WAGES,  matcher[2] - COLOR_WAGES], [matcher[0] + COLOR_WAGES, matcher[1] + COLOR_WAGES,  matcher[2] + COLOR_WAGES])
    color_lower = array( lower)
    color_upper = array( upper)

    mask = cv.inRange(img, color_lower, color_upper)
    if mask.any():
        return True
    return False