from utils.config import dict, random_timeout
from time import sleep
from wrappers.win32api_wrapper import *
from wrappers.logging_wrapper import debug

def fish_notice():
    notice_timeout = random_timeout(dict['fishing']['timeouts']['notice'])
    debug("Press mouse key for: {} s".format(notice_timeout))
    press_mouse_key()
    sleep(notice_timeout)
    release_mouse_key()

def reel_fish():
    reel_timeout = random_timeout(dict['fishing']['timeouts']['reeling'])
    debug("Press mouse key for: {} s".format(reel_timeout))
    press_mouse_key()
    sleep(reel_timeout)
    release_mouse_key()

def pause():
    pause_timeout = random_timeout(dict['fishing']['timeouts']['pause'])
    debug("Pause for: {} s".format(pause_timeout))
    sleep(pause_timeout)

def cast():
    cast_timeout = random_timeout(dict['fishing']['timeouts']['cast'])
    debug("Pause for: {} s".format(cast_timeout))
    press_mouse_key()
    sleep(cast_timeout)
    release_mouse_key()
    debug("Pause for: 5 s")
    sleep(5)

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
    press_key('F3')
    release_key('F3')
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
