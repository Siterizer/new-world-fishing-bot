import utils.global_variables as gv
from functionality.fishing_actions import fishing_loop
from utils.global_variables import *
from functools import partial


def start_fishing(button):
    changeFishingState(button)
    fishing_loop()

def changeFishingState(button):
    gv.continue_fishing = not gv.continue_fishing
    if(gv.continue_fishing):
        button.configure(text = "Stop fishing")
        button.configure(command = partial(changeFishingState, button))
        return
    button.configure(text = "Start fishing")
    button.configure(command = partial(start_fishing, button))
