from functionality.fishing_actions import fishing_loop
from utils.global_variables import *
from functools import partial


def start_fishing(button):
    changeFishingState(button)
    fishing_loop()

def changeFishingState(button):
    negate_fishing_state()
    if(fishing_state()):
        button.configure(text = "Stop fishing")
        button.configure(command = partial(changeFishingState, button))
        return
    button.configure(text = "Start fishing")
    button.configure(command = partial(start_fishing, button))
