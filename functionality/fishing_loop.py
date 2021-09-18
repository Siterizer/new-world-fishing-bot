import utils.global_variables as gv
from functionality.fishing_actions import *
from wrappers.model_wrapper import get_model_result
from wrappers.logging_wrapper import info, debug
from time import time, sleep


def fishing_loop():
    debug('starting new loop')
    gv.last_results.add(call_appropriate_fishing_action())
    if(gv.last_results.is_full_of('0')):
        if(dict['repairing']['enable'].get() == 1):
            should_repair_in = -1 * (int(time()) - gv.last_repair_time - dict['repairing']['every'].get())
            debug("Repair in: " + str(should_repair_in))
            if(should_repair_in < 0):
                gv.last_repair_time = int(time())
                info("Repairing")
                repairing()
    if (gv.continue_fishing):
        gv.root.after(int(dict['fishing']['timeouts']['loop']*1000), fishing_loop)



def call_appropriate_fishing_action():
    result_from_model = get_model_result(dict['fishing']['x'].get(), dict['fishing']['y'].get(),
                                         dict['fishing']['width'].get(), dict['fishing']['height'].get())
    if(gv.last_results.get_last_value() != result_from_model and result_from_model != '1' ):
        return result_from_model
    if result_from_model == '0': # 0 - model does not match any data (not fish captured yet)
        info("Waiting for fish...")
        return '0'
    elif result_from_model == '1': # 1 - model noticed a fish(left click to initiate fishing)
        info("Found a fish!")
        fish_notice()
        return '1'
    elif result_from_model == '2': #2 - model matched the green icon (reeling a fish in)
        info("Reeling a fish")
        reel_fish()
        return '2'
    elif result_from_model == '3': #3 - model matched the orange/red icon (click and wait 2sec)
        info("Pause fishing")
        pause()
        return '3'
