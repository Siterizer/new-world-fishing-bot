import sys
from os import path
import configparser
import cv2 as cv

def rootPath():
    try:
        return sys._MEIPASS
    except Exception:
        return path.abspath(".")


ROOT_DIR = rootPath()
CONFIG_PATH = path.join(ROOT_DIR, "resources\\config.yml")
WAITING_FOR_FISH = path.join(ROOT_DIR, "resources\\waiting_for_fish.jpg")
FISH_NOTICED = path.join(ROOT_DIR, "resources\\fish_noticed.png")
ICON_PATH = path.join(ROOT_DIR, "resources\\icon.ico")
COLOR_WAGES = 4



def get_image_recognition_images():
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

    return prepare_img(FISH_NOTICED, scaleX, scaleY),prepare_img(WAITING_FOR_FISH, scaleX, scaleY)

def prepare_img(path, scaleX, scaleY):
    image = cv.imread(path)
    width = int(image.shape[1] * scaleX)
    height = int(image.shape[1] * scaleY)
    dim = (width, height)
    image = cv.resize(image, dim, cv.INTER_LINEAR)
    return cv.cvtColor(image, cv.COLOR_BGR2GRAY)