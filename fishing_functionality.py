from config import dict
from functools import partial
from tkinter import *
from pyautogui_wrapper import *
from datetime import datetime
import time

continue_fishing = False
counter = 0

def start_fishing(root, button):
    global continue_fishing
    button.configure(text = "Stop fishing")
    button.configure(command = partial(stop_fishing, root, button))
    continue_fishing = True
    main_loop(root)


def main_loop(root):
    global counter
    global continue_fishing
    counter += 1
    print(counter)
    if(counter % 10 == 0):
        repairing()
    fishing()
    if (continue_fishing):
        root.after(100, main_loop, root)


def stop_fishing(root, button):
    global continue_fishing
    continue_fishing = False
    button.configure(text = "Start fishing")
    button.configure(command = partial(start_fishing, root, button))

def repairing():
    press_key('tab') #Open equipment
    release_key('tab') #release key
    time.sleep(2) #Wait equipment loads
    press_key('r') #Press repair hotkey
    click_mouse_with_coordinates(dict['repairing']['x'].get(), dict['repairing']['y'].get())
    time.sleep(2) #Wait 2s until the rod is finished repairing
    release_key('r') #release key
    press_key('escape') #escape equipment
    release_key('escape') #release key

def fishing():
    cropped_screenshot = get_screenshot(dict['fishing']['x'].get(), dict['fishing']['y'].get(), dict['fishing']['width'].get(), dict['fishing']['height'].get())
    save_screenshot(cropped_screenshot)#UNCOMMENT ONLY WHEN YOU NEED TO COLLECT YOUR SCREENSHOTS

    #AI model WIP
    result_from_model = 0#model(cropped_screenshot)
    #AI model WIP

    if result_from_model == 0: # 0 - model does not match any data (not fish captured yet)
        return
    elif result_from_model == 1: # 1 - model noticed a fish(left click to start game)
        initiate_fishing()
        return
    elif result_from_model == 2: #2 - model matched the green icon (reeling a fish in)
        reel_fish()
        return
    elif result_from_model == 3: #2 - model matched the yellow/red icon (wait 2sec)
        time.sleep(2)
        return

def initiate_fishing():
    click_mouse_with_coordinates(dict['fishing']['x'].get() + dict['fishing']['width'].get()//2,
                                dict['fishing']['y'].get() + dict['fishing']['height'].get()//2)

def reel_fish():
    press_mouse_key()
    time.sleep(2)
    release_mouse_key()


def save_screenshot(screenshot):
    actual_time = datetime.utcnow().strftime('%Y_%m_%d_%H_%M_%S_%f')
    screenshot.save(r"G:\new-world-bot\saved_data\screenshots\\"+ actual_time + ".png")





