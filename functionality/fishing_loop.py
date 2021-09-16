import utils.global_variables as gv
from functionality.fishing_actions import *
from wrappers.model_wrapper import get_model_result
from wrappers.pyautogui_wrapper import *
from time import time, sleep


def fishing_loop():
    gv.last_results.add(call_appropriate_fishing_action())
    if(gv.last_results.is_full_of('0')):
        if(dict['repairing']['enable'].get() == 1):
            if(int(time()) > gv.last_repair_time + dict['repairing']['every'].get()):
                gv.last_repair_time = int(time.time())
                repairing()
    if (gv.continue_fishing):
        gv.root.after(int(dict['fishing']['timeouts']['loop']*1000), fishing_loop)



def call_appropriate_fishing_action():
    screenshot = get_screenshot(dict['fishing']['x'].get(), dict['fishing']['y'].get(),
                                dict['fishing']['width'].get(), dict['fishing']['height'].get())
    #save_screenshot(screenshot) #UNCOMMENT ONLY WHEN YOU NEED TO SAVE YOUR SCREENSHOTS (model training etc.)
    result_from_model = get_model_result(screenshot)
    if(gv.last_results.get_last_value() != result_from_model and result_from_model != '1' ):
        return result_from_model
    if result_from_model == '0': # 0 - model does not match any data (not fish captured yet)
        print("Waiting for fish...")
        return '0'
    elif result_from_model == '1': # 1 - model noticed a fish(left click to initiate fishing)
        print("Found a fish!")
        fish_notice()
        return '1'
    elif result_from_model == '2': #2 - model matched the green icon (reeling a fish in)
        print("Reeling a fish")
        reel_fish()
        return '2'
    elif result_from_model == '3': #3 - model matched the orange/red icon (click and wait 2sec)
        print("Pause fishing")
        pause()
        return '3'
