from global_variables import *
from resources.config import dict
from wrappers.model_wrapper import get_model_result
from wrappers.pyautogui_wrapper import *



def fishing_loop(root):
    results().add(fishing())
    if(results().is_full_of('0')):
        if(dict['repairing']['enable'].get() == 1):
            if(int(time.time()) > get_last_repair_time()+ dict['repairing']['every'].get()):
                update_last_repair_time()
                repairing()
    if (fishing_state()):
        root.after(10, fishing_loop, root)


def repairing():
    print('repair')
    #End fishing cycle
    time.sleep(1)
    press_key('f3')
    release_key('f3')
    time.sleep(1)

    #Open inventory
    press_key('tab')
    release_key('tab')
    time.sleep(3)

    #Press 'r' and click on fishing rod
    press_key('r')
    time.sleep(1)
    click_mouse_with_coordinates(dict['repairing']['x'].get(), dict['repairing']['y'].get(), 0)
    time.sleep(0.1)
    release_key('r')

    #Confirm repair
    time.sleep(1)
    press_key('e')
    release_key('e')
    time.sleep(1)

    #Close inventory
    press_key('escape')
    release_key('escape')

    #Grab again fishing rod
    time.sleep(1)
    press_key('f3')
    release_key('f3')

def fishing():
    screenshot = get_screenshot(dict['fishing']['x'].get(), dict['fishing']['y'].get(),
                                dict['fishing']['width'].get(), dict['fishing']['height'].get())
    #save_screenshot(screenshot) #UNCOMMENT ONLY WHEN YOU NEED TO SAVE YOUR SCREENSHOTS (model training etc.)
    result_from_model = get_model_result(screenshot)
    if(results().get_last_value() != result_from_model and result_from_model != '1' ):
        return result_from_model
    if result_from_model == '0': # 0 - model does not match any data (not fish captured yet)
        print("Waiting for fish...")
        return '0'
    elif result_from_model == '1': # 1 - model noticed a fish(left click to initiate fishing)
        print("Found a fish!")
        reel_fish()
        return '1'
    elif result_from_model == '2': #2 - model matched the green icon (reeling a fish in)
        print("Reeling a fish")
        reel_fish()
        return '2'
    elif result_from_model == '3': #3 - model matched the yellow/red icon (wait 2sec)
        print("Pause fishing")
        initiate_game()
        time.sleep(2)
        return '3'


def initiate_game():
    press_mouse_key()
    time.sleep(0.1)
    release_mouse_key()

def reel_fish():
    press_mouse_key()
    time.sleep(1.5)
    release_mouse_key()