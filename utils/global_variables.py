from utils.LastResults import LastResults
from os import path, environ
import sys
from time import time
from tkinter import Tk


ROOT_DIR  = getattr(sys, '_MEIPASS', path.dirname(path.abspath(__file__)))
CONFIG_PATH = path.join(ROOT_DIR, 'resources\config.yml')
WAITING_FOR_FISH = path.join(ROOT_DIR, 'resources\\waiting_for_fish.jpg')
FISH_NOTICED = path.join(ROOT_DIR, 'resources\\fish_noticed.jpg')

continue_fishing = False
last_repair_time = int(time())
last_results = LastResults()
root = Tk()
