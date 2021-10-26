from utils.config import dict, random_timeout
from time import sleep
from wrappers.win32api_wrapper import *
from wrappers.logging_wrapper import info, debug
import utils.global_variables as gv
import math

def fish_notice(event):
    notice_timeout = random_timeout(dict['fishing']['timeouts']['notice'])
    debug("Press mouse key for: {} s".format(notice_timeout))
    if (gv.continue_fishing):
        press_mouse_key()
        event.wait(notice_timeout)
        release_mouse_key()

def reel_fish(event):
    reel_timeout = random_timeout(dict['fishing']['timeouts']['reeling'])
    debug("Press mouse key for: {} s".format(reel_timeout))
    if (gv.continue_fishing):
        press_mouse_key()
        event.wait(reel_timeout)
        release_mouse_key()

def pause(event):
    pause_timeout = random_timeout(dict['fishing']['timeouts']['pause'])
    debug("Pause for: {} s".format(pause_timeout))
    if (gv.continue_fishing):
        event.wait(pause_timeout)

def cast(event):
    cast_timeout = random_timeout(dict['fishing']['timeouts']['cast'])
    debug("Pause for: 6 s")
    if (gv.continue_fishing):
        event.wait(6)

    if (gv.continue_fishing):
        debug("release b")
        release_key('b')

    if (gv.continue_fishing):
        debug("Pause for: 1 s")
        event.wait(1)

    if (gv.continue_fishing):
        debug("Pause for: {} s".format(cast_timeout))
        press_mouse_key()
        event.wait(cast_timeout)
        release_mouse_key()

    if (gv.continue_fishing):
        debug("Pause for: 5 s")
        event.wait(5)

    if (gv.continue_fishing):
        debug("press b")
        press_key('b')

def repairing(event):
    release_key('b')
    arm_disarm_timeout = random_timeout(dict['repairing']['timeouts']['arm_disarm'])
    debug("Disarm fishing rod. Total time: {} s".format(arm_disarm_timeout))
    arm_disarm_fishing_rod(event, arm_disarm_timeout)

    inventory_timeout = random_timeout(dict['repairing']['timeouts']['inventory'])
    debug("Open inventory. Total time: {} s".format(inventory_timeout))
    open_close_inventory(event, inventory_timeout)

    repair_timeout = random_timeout(dict['repairing']['timeouts']['repair'])
    debug("Repair fishing rod. Total time: {} s".format(repair_timeout))
    repair(event, repair_timeout)

    confirm_timeout = random_timeout(dict['repairing']['timeouts']['confirm'])
    debug("Confirm repair. Total time: {} s".format(confirm_timeout))
    confirm_repair(event, confirm_timeout)

    debug("Close inventory. Total time: {} s".format(inventory_timeout))
    open_close_inventory(event, inventory_timeout)

    debug("Arm fishing rod. Total time: {} s".format(arm_disarm_timeout))
    arm_disarm_fishing_rod(event, arm_disarm_timeout)

    move_around = random_timeout(dict['repairing']['timeouts']['move_around'])
    debug("Move to prevent AFK kick. Total time:  {} s".format(move_around))
    move_left_right(event, move_around)

def arm_disarm_fishing_rod(event, timeout):
    if (gv.continue_fishing):
        event.wait(timeout)
        press_key('F3')
        release_key('F3')

    if (gv.continue_fishing):
        event.wait(timeout)

def open_close_inventory(event, timeout):
    if (gv.continue_fishing):
        event.wait(timeout)
        press_key('tab')
        release_key('tab')
    if (gv.continue_fishing):
        event.wait(timeout)

def repair(event, timeout):
    if (gv.continue_fishing):
        event.wait(timeout)
        press_key('r')
        event.wait(0.1)
        click_mouse_with_coordinates(dict['repairing']['x'].get(), dict['repairing']['y'].get())
        event.wait(0.1)
        release_key('r')
    if (gv.continue_fishing):
        event.wait(timeout)

def confirm_repair(event, timeout):
    if (gv.continue_fishing):
        event.wait(timeout)
        press_key('e')
        event.wait(0.1)
        release_key('e')
    if (gv.continue_fishing):
        event.wait(timeout)

def move_left_right(event, timeout):
    if (gv.continue_fishing):
        press_key('a')
        event.wait(timeout)
        release_key('a')
    if (gv.continue_fishing):
        event.wait(1.0)
        press_key('d')
        event.wait(timeout)
        release_key('d')

def select_bait(event):
    if (gv.continue_fishing):
        release_key('b')
        debug("Bait selection.")
        press_key('r')
        event.wait(0.1)
        release_key('r')

    if (gv.continue_fishing):
        bait_select_timeout = random_timeout(dict['bait']['timeouts']['select'])
        debug("Bait select. Total time: {} s".format(bait_select_timeout))
        press_on_bait(event, bait_select_timeout)

    if (gv.continue_fishing):
        confirm_timeout = random_timeout(dict['bait']['timeouts']['confirm'])
        debug("Confirm bait selection. Total time: {} s".format(confirm_timeout))
        press_equip_bait(event, confirm_timeout)

def press_on_bait(event, timeout):

    if (gv.continue_fishing):
        event.wait(timeout)
        click_mouse_with_coordinates(dict['bait']['bait_x'].get(), dict['bait']['bait_y'].get())
    if (gv.continue_fishing):
        event.wait(timeout)

def press_equip_bait(event, timeout):
    if (gv.continue_fishing):
        event.wait(timeout)
        click_mouse_with_coordinates(dict['bait']['equip_button_x'].get(), dict['bait']['equip_button_y'].get())
    if (gv.continue_fishing):
        event.wait(timeout)
    # waiting for animation to finish
    if (gv.continue_fishing):
        event.wait(1)