from functionality.fishing_actions import fishing_loop
from global_variables import *
from functools import partial

def start_fishing(root, button):
    changeFishingState(root, button)
    fishing_loop(root)

def changeFishingState(root, button):
    negate_fishing_state()
    if(fishing_state()):
        button.configure(text = "Stop fishing")
        button.configure(command = partial(changeFishingState, root, button))
        return
    button.configure(text = "Start fishing")
    button.configure(command = partial(start_fishing, root, button))
