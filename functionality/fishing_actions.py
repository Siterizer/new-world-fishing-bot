from utils.config import dict
from time import sleep
from wrappers.pyautogui_wrapper import *

def fish_notice():
    press_mouse_key()
    sleep(dict['fishing']['timeouts']['notice'])
    release_mouse_key()

def reel_fish():
    press_mouse_key()
    sleep(dict['fishing']['timeouts']['reeling'])
    release_mouse_key()

def pause():
    sleep(dict['fishing']['timeouts']['pause'])

def repairing():
    print('repair')
    arm_disarm_fishing_rod()
    open_close_inventory()
    repair()
    confirm_repair()
    open_close_inventory()
    arm_disarm_fishing_rod()

def arm_disarm_fishing_rod():
    sleep(dict['repairing']['timeouts']['arm_disarm'])
    press_key('f3')
    release_key('f3')
    sleep(dict['repairing']['timeouts']['arm_disarm'])

def open_close_inventory():
    sleep(dict['repairing']['timeouts']['inventory'])
    press_key('tab')
    release_key('tab')
    sleep(dict['repairing']['timeouts']['inventory'])

def repair():
    sleep(dict['repairing']['timeouts']['repair'])
    press_key('r')
    sleep(0.1)
    click_mouse_with_coordinates(dict['repairing']['x'].get(), dict['repairing']['y'].get())
    sleep(0.1)
    release_key('r')
    sleep(dict['repairing']['timeouts']['repair'])

def confirm_repair():
    sleep(dict['repairing']['timeouts']['confirm'])
    press_key('e')
    sleep(0.1)
    release_key('e')
    sleep(dict['repairing']['timeouts']['confirm'])
