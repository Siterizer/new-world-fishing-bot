from utils.LastResults import LastResults
from os import path, environ
import sys
from time import time
from tkinter import Tk


ROOT_DIR  = getattr(sys, '_MEIPASS', path.dirname(path.abspath(__file__)))
CONFIG_PATH = path.join(ROOT_DIR, '..\\resources\config.yml')
MODEL_PATH = path.join(ROOT_DIR, '..\\resources\model\\')
SCREENSHOTS_PATH = path.join(ROOT_DIR, '..\\saved_data\screenshots\\')

continue_fishing = False
last_repair_time = int(time())
last_results = LastResults()
root = Tk()
