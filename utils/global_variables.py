from functionality.LastResults import *
import os
import time
from tkinter import Tk

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
CONFIG_PATH = os.path.join(ROOT_DIR, 'config.yml')
MODEL_PATH = os.path.join(ROOT_DIR, 'model\\')
SCREENSHOTS_PATH = os.path.join(ROOT_DIR, '..\saved_data\screenshots\\')

continue_fishing = False
last_repair_time = int(time.time())
last_results = LastResults()
root = Tk()
