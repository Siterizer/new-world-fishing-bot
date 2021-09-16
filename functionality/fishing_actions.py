from utils.config import dict
from time import sleep
from wrappers.pyautogui_wrapper import *
from wrappers.logging_wrapper import debug

def fish_notice():
    debug("Press mouse key for: {} s".format(dict['fishing']['timeouts']['notice']))
    press_mouse_key()
    sleep(dict['fishing']['timeouts']['notice'])
    release_mouse_key()

def reel_fish():
    debug("Press mouse key for: {} s".format(dict['fishing']['timeouts']['reeling']))
    press_mouse_key()
    sleep(dict['fishing']['timeouts']['reeling'])
    release_mouse_key()

def pause():
    debug("Pause for: {} s".format(dict['fishing']['timeouts']['pause']))
    sleep(dict['fishing']['timeouts']['pause'])

def repairing():
    debug("Disarm fishing rod. Total time: {} s".format(dict['repairing']['timeouts']['arm_disarm']))
    arm_disarm_fishing_rod()
    debug("Open inventory. Total time: {} s".format(dict['repairing']['timeouts']['inventory']))
    open_close_inventory()
    debug("Repair fishing rod. Total time: {} s".format(dict['repairing']['timeouts']['repair']))
    repair()
    debug("Confirm repair. Total time: {} s".format(dict['repairing']['timeouts']['confirm']))
    confirm_repair()
    debug("Close inventory. Total time: {} s".format(dict['repairing']['timeouts']['confirm']))
    open_close_inventory()
    debug("Arm fishing rod. Total time: {} s".format(dict['repairing']['timeouts']['confirm']))
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
