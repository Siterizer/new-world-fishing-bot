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
    debug("Pause for: 6 s")
    sleep(6)
    debug("release b")
    release_key('b')
    debug("Pause for: 1 s")
    sleep(1)
    debug("Pause for: {} s".format(cast_timeout))
    press_mouse_key()
    sleep(cast_timeout)
    release_mouse_key()
    debug("Pause for: 5 s")
    sleep(5)
    debug("press b")
    press_key('b')

def repairing():
    release_key('b')
    arm_disarm_timeout = random_timeout(dict['repairing']['timeouts']['arm_disarm'])
    debug("Disarm fishing rod. Total time: {} s".format(arm_disarm_timeout))
    arm_disarm_fishing_rod(arm_disarm_timeout)

    inventory_timeout = random_timeout(dict['repairing']['timeouts']['inventory'])
    debug("Open inventory. Total time: {} s".format(inventory_timeout))
    open_close_inventory(inventory_timeout)

    repair_timeout = random_timeout(dict['repairing']['timeouts']['repair'])
    debug("Repair fishing rod. Total time: {} s".format(repair_timeout))
    repair(repair_timeout)

    confirm_timeout = random_timeout(dict['repairing']['timeouts']['confirm'])
    debug("Confirm repair. Total time: {} s".format(confirm_timeout))
    confirm_repair(confirm_timeout)

    debug("Close inventory. Total time: {} s".format(inventory_timeout))
    open_close_inventory(inventory_timeout)

    debug("Arm fishing rod. Total time: {} s".format(arm_disarm_timeout))
    arm_disarm_fishing_rod(arm_disarm_timeout)

    move_around = random_timeout(dict['repairing']['timeouts']['move_around'])
    debug("Move to prevent AFK kick. Total time:  {} s".format(move_around))
    move_left_right(move_around)

def arm_disarm_fishing_rod(timeout):
    sleep(timeout)
    press_key('F3')
    release_key('F3')
    sleep(timeout)

def open_close_inventory(timeout):
    sleep(timeout)
    press_key('tab')
    release_key('tab')
    sleep(timeout)

def repair(timeout):
    sleep(timeout)
    key = 'r' if dict['repairing']['kit'].get() == 0 else 't'
    debug("Repairing with key: {}".format(key))
    press_key(key)
    sleep(0.1)
    click_mouse_with_coordinates(dict['repairing']['x'].get(), dict['repairing']['y'].get())
    sleep(0.1)
    release_key(key)
    sleep(timeout)

def confirm_repair(timeout):
    sleep(timeout)
    press_key('e')
    sleep(0.1)
    release_key('e')
    sleep(timeout)

def move_left_right(timeout):
    press_key('a')
    sleep(timeout)
    release_key('a')
    sleep(1.0)
    press_key('d')
    sleep(timeout)
    release_key('d')

def select_bait():
    release_key('b')

    debug("Bait selection.")
    press_key('r')
    sleep(0.1)
    release_key('r')

    bait_select_timeout = random_timeout(dict['bait']['timeouts']['select'])
    debug("Bait select. Total time: {} s".format(bait_select_timeout))
    press_on_bait(bait_select_timeout)

    confirm_timeout = random_timeout(dict['bait']['timeouts']['confirm'])
    debug("Confirm bait selection. Total time: {} s".format(confirm_timeout))
    press_equip_bait(confirm_timeout)

def press_on_bait(timeout):
    sleep(timeout)
    click_mouse_with_coordinates(dict['bait']['bait_x'].get(), dict['bait']['bait_y'].get())
    sleep(timeout)

def press_equip_bait(timeout):
    sleep(timeout)
    click_mouse_with_coordinates(dict['bait']['equip_button_x'].get(), dict['bait']['equip_button_y'].get())
    sleep(timeout)
    # waiting for animation to finish
    sleep(1)