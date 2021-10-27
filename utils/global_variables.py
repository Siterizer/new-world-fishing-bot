import sys
from os import path


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
