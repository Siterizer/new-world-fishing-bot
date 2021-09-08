from resources.config import dict, save_data
from functools import partial
from tkinter import *
from wrappers.pyautogui_wrapper import *
from datetime import datetime
import time

continue_fishing = False
counter = 0

def start_fishing(root, button):
    changeFishingState(root, button)
    main_loop(root)

def changeFishingState(root, button):
    global continue_fishing
    continue_fishing = not continue_fishing
    if(continue_fishing):
        button.configure(text = "Stop fishing")
        button.configure(command = partial(changeFishingState, root, button))
        return
    button.configure(text = "Start fishing")
    button.configure(command = partial(start_fishing, root, button))


def main_loop(root):
    global counter
    global continue_fishing
    counter += 1
    #if(counter % 10 == 0):
        #repairing()
    fishing()
    if (continue_fishing):
        root.after(100, main_loop, root)



def repairing():
    press_key('tab')
    release_key('tab')
    time.sleep(2)
    press_key('r')
    click_mouse_with_coordinates(dict['repairing']['x'].get(), dict['repairing']['y'].get())
    time.sleep(2)
    release_key('r')
    press_key('escape')
    release_key('escape')

def fishing():
    result_from_model = '0'#screen_recognize(dict['fishing']['x'].get(), dict['fishing']['y'].get(), dict['fishing']['width'].get(), dict['fishing']['height'].get())

    print(result_from_model)
    if result_from_model == '0': # 0 - model does not match any data (not fish captured yet)
        return
    elif result_from_model == '1': # 1 - model noticed a fish(left click to initiate fishing)
        initiate_fishing()
        return
    elif result_from_model == '2': #2 - model matched the green icon (reeling a fish in)
        reel_fish()
        return
    elif result_from_model == '3': #2 - model matched the yellow/red icon (wait 2sec)
        time.sleep(2)
        return

def initiate_fishing():
    click_mouse_with_coordinates(dict['fishing']['x'].get() + dict['fishing']['width'].get()//2,
                                dict['fishing']['y'].get() + dict['fishing']['height'].get()//2)

def reel_fish():
    press_mouse_key()
    time.sleep(2)
    release_mouse_key()






