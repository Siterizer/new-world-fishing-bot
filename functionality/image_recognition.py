from utils.config import config_dict
from numpy import array
import cv2 as cv
from PIL import ImageGrab
from utils.global_variables import WAITING_FOR_FISH, FISH_NOTICED
from os import path
import configparser

# Baseline Resolution at which the templates were recorded
base_width = 1920
base_height = 1080
# Get Game Resolution from user_preload_settings.cfg
nw_config_path = path.expandvars(r"%APPDATA%\AGS\New World\user_preload_settings.cfg")
if path.isfile(nw_config_path):
    config = configparser.ConfigParser(allow_no_value=True)
    with open(nw_config_path, "r") as f:
        config_string = "[dummy_section]\n" + f.read()
    config.read_string(config_string)
    scaleX = int(config["dummy_section"]["r_Width"]) / base_width
    scaleY = int(config["dummy_section"]["r_Height"]) / base_height
else:
    scaleX = 1
    scaleY = 1

NOTHING = cv.imread(WAITING_FOR_FISH)
width = int(NOTHING.shape[1] * scaleX)
height = int(NOTHING.shape[1] * scaleY)
dim = (width, height)
NOTHING = cv.resize(NOTHING, dim, cv.INTER_LINEAR)
NOTICE = cv.imread(FISH_NOTICED)
width = int(NOTICE.shape[1] * scaleX)
height = int(NOTICE.shape[1] * scaleY)
dim = (width, height)
NOTICE = cv.resize(NOTICE, dim, cv.INTER_LINEAR)
REEL_COLOR = config_dict["colors"]["green"]
WAIT_COLOR_BROWN = config_dict["colors"]["brown"]
WAIT_COLOR_RED = config_dict["colors"]["red"]
COLOR_WAGES = 7


def image_recognition_result(x, y, width, height):
    region = (x, y, x + width, y + height)
    img = array(ImageGrab.grab(bbox=region))
    img_cv = cv.cvtColor(img, cv.COLOR_RGB2BGR)
    res = cv.matchTemplate(img_cv, NOTICE, eval("cv.TM_CCOEFF_NORMED"))
    if (res >= 0.7).any():
        return "1"
    res = cv.matchTemplate(img_cv, NOTHING, eval("cv.TM_CCOEFF_NORMED"))
    if (res >= 0.7).any():
        return "0"

    if pixel_match(img, REEL_COLOR):
        return "2"
    if pixel_match(img, WAIT_COLOR_BROWN):
        return "3"
    if pixel_match(img, WAIT_COLOR_RED):
        return "4"
    return "5"


def pixel_match(img, matcher):
    lower, upper = (
        [matcher[0] - COLOR_WAGES, matcher[1] - COLOR_WAGES, matcher[2] - COLOR_WAGES],
        [matcher[0] + COLOR_WAGES, matcher[1] + COLOR_WAGES, matcher[2] + COLOR_WAGES],
    )
    color_lower = array(lower)
    color_upper = array(upper)

    mask = cv.inRange(img, color_lower, color_upper)
    if mask.any():
        return True
    return False
