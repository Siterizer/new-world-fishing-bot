from utils.config import dict
from wrappers.pyautogui_wrapper import *

def initiate_game():
    press_mouse_key()
    time.sleep(0.1)
    release_mouse_key()

def reel_fish():
    press_mouse_key()
    time.sleep(1.5)
    release_mouse_key()

def repairing():
    print('repair')
    arm_disarm_fishing_rod()
    open_close_inventory()
    repair()
    confirm_repair()
    open_close_inventory()
    arm_disarm_fishing_rod()

def arm_disarm_fishing_rod():
    time.sleep(1)
    press_key('f3')
    release_key('f3')
    time.sleep(1)

def open_close_inventory():
    time.sleep(1)
    press_key('tab')
    release_key('tab')
    time.sleep(1)

def repair():
    time.sleep(1)
    press_key('r')
    time.sleep(0.1)
    click_mouse_with_coordinates(dict['repairing']['x'].get(), dict['repairing']['y'].get())
    time.sleep(0.1)
    release_key('r')
    time.sleep(1)

def confirm_repair():
    time.sleep(1)
    press_key('e')
    time.sleep(0.1)
    release_key('e')
    time.sleep(1)
