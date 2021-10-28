from utils.LastResults import LastResults
from os import path
import sys
from tkinter import Label
from time import time
from tkinter import Tk
from datetime import datetime

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

continue_fishing = False
start_time = datetime.now()
loop_count = 0
total_minutes = 0;
total_casts = 0
total_found = 0
total_caught = 0
last_detected_green_before_casting = False
last_repair_time = int(time())
last_results = LastResults()
root = Tk()

minutes_text_label = Label(root, text = "Time (minutes): 0")
casts_text_label = Label(root, text = "Casts: 0")
found_text_label = Label(root, text = "Found: 0")
caught_text_label = Label(root, text = "Caught: 0")