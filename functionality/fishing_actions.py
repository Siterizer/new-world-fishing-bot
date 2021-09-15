from utils.config import dict
from time import sleep
from wrappers.pyautogui_wrapper import *

def initiate_game():
    press_mouse_key()
    sleep(0.1)
    release_mouse_key()

def reel_fish():
    press_mouse_key()
    sleep(1.5)
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
    sleep(1)
    press_key('f3')
    release_key('f3')
    sleep(1)

def open_close_inventory():
    sleep(1)
    press_key('tab')
    release_key('tab')
    sleep(1)

def repair():
    sleep(1)
    press_key('r')
    sleep(0.1)
    click_mouse_with_coordinates(dict['repairing']['x'].get(), dict['repairing']['y'].get())
    sleep(0.1)
    release_key('r')
    sleep(1)

def confirm_repair():
    sleep(1)
    press_key('e')
    sleep(0.1)
    release_key('e')
    sleep(1)
