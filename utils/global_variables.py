from utils.LastResults import LastResults
from os import path
import sys
from time import time
from tkinter import Tk
import ctypes

def rootPath():
    try:
        return sys._MEIPASS
    except Exception:
        return path.abspath(".")

ROOT_DIR  = rootPath()
CONFIG_PATH = path.join(ROOT_DIR, 'resources\config.yml')
WAITING_FOR_FISH = path.join(ROOT_DIR, 'resources\\waiting_for_fish.jpg')
FISH_NOTICED = path.join(ROOT_DIR, 'resources\\fish_noticed.jpg')
ICON_PATH = path.join(ROOT_DIR, 'resources\\icon.ico')
 
ctypes.windll.shcore.SetProcessDpiAwareness(1)
continue_fishing = False
last_repair_time = int(time())
last_results = LastResults()
root = Tk()
