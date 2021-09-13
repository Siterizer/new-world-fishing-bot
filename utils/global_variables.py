from functionality.LastResults import *
import os
import time
from tkinter import Tk

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
CONFIG_PATH = os.path.join(ROOT_DIR, 'config.yml')
MODEL_PATH = os.path.join(ROOT_DIR, 'model\\')


def init_variables():
    global root
    root = Tk()

    global continue_fishing
    continue_fishing = False

    global last_results
    last_results = LastResults()
    
    global last_repair_time
    last_repair_time = int(time.time())

def get_root():
    global root
    return root

def fishing_state():
    global continue_fishing
    return continue_fishing

def negate_fishing_state():
    global continue_fishing
    continue_fishing = not continue_fishing

def results():
    global last_results
    return last_results
    
def get_last_repair_time():
    global last_repair_time
    return last_repair_time
    
def update_last_repair_time():
    global last_repair_time
    last_repair_time = int(time.time())