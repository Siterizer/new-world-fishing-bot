from config import dict
from functools import partial
from tkinter import *
from datetime import datetime
import pyautogui
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
    if(counter % 10 == 0):
        repair()
    fishing()
    if (continue_fishing):
        root.after(100, main_loop, root)


def stop_fishing(root, button):
    global continue_fishing
    continue_fishing = False
    button.configure(text = "Start fishing")
    button.configure(command = partial(start_fishing, root, button))

def repair():
    pyautogui.keyDown('tab') #Open equipment
    pyautogui.keyUp('tab') #release key
    time.sleep(2) #Wait equipment loads
    pyautogui.keyDown('r') #Press repair hotkey
    pyautogui.click(x=dict['repairing']['x'].get(), y=dict['repairing']['y'].get()) #Repair rod
    time.sleep(2) #Wait 2s until the rod is finished repairing
    pyautogui.keyUp('r') #release key
    pyautogui.keyDown('escape') #escape equipment
    pyautogui.keyUp('escape') #release key

def fishing():
    cropped_screenshot = pyautogui.screenshot(region=(dict['fishing']['x'].get(), dict['fishing']['y'].get(),
    dict['fishing']['width'].get(), dict['fishing']['height'].get()))
    #save_screenshot(cropped_screenshot)#UNCOMMENT ONLY WHEN YOU NEED TO COLLECT YOUR SCREENSHOTS

    #AI model WIP
    result_from_model = 0#model(cropped_screenshot)
    #AI model WIP

    if result_from_model == 0: # 0 - model does not match any data (not fish captured yet)
        return
    elif result_from_model == 1: # 1 - model noticed a fish(left click to start game)
        start_game()
        return
    elif result_from_model == 2: #2 - model matched the green icon (reeling a fish in)
        reel_fish()
        return
    elif result_from_model == 3: #2 - model matched the yellow/red icon (wait 2sec)
        time.sleep(2)
        return

def start_game():
    pyautogui.click(x=(dict['fishing']['x'].get() + dict['fishing']['width'].get()//2), y=(dict['fishing']['y'].get() + dict['fishing']['height'].get()//2))

def reel_fish():
    pyautogui.mouseDown()
    time.sleep(2)
    pyautogui.mouseUp()


def save_screenshot(screenshot):
    actual_time = datetime.utcnow().strftime('%Y_%m_%d_%H_%M_%S_%f')
    screenshot.save(r"G:\new-world-bot\saved_data\\"+ actual_time + ".png")





