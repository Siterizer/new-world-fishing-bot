from tkinter import Toplevel, Canvas, IntVar
from functools import partial
from utils.config import dict, save_data
from functionality.fishing_loop import fishing_loop
import utils.global_variables as gv


def popup_rectangle_window(button, x, y, width, height):
    window = Toplevel()
    window.resizable(False, False)
    window.attributes('-fullscreen', True)
    window.wm_attributes('-transparentcolor', window['bg'])
    canvas = Canvas(window, width=10000, height=10000)
    canvas.create_rectangle(x.get(), y.get(), x.get()+width.get(), y.get()+height.get(), outline="green", width=5)
    canvas.pack()
    button.configure(command = partial(destroy_rectangle_window, window, button, x, y, width, height))

def destroy_rectangle_window(window, button, x, y, width, height):
    window.destroy()
    button.configure(command = partial(popup_rectangle_window, button, x,y,width,height))

def on_closing():
    save_data()
    gv.root.destroy()

def change_repair_button_state(button):
    if (dict['repairing']['enable'].get() == 1):
        button.configure(text="OFF")
        button.configure(bg="red")
        dict['repairing']['enable'] = IntVar(value=0)
    else:
        button.configure(text="ON ")
        button.configure(bg="green")
        dict['repairing']['enable'] = IntVar(value=1)

def changeFishingState(button):
    gv.continue_fishing = not gv.continue_fishing
    if(gv.continue_fishing):
        button.configure(text = "Stop fishing")
        button.configure(command = partial(changeFishingState, button))
        return
    button.configure(text = "Start fishing")
    button.configure(command = partial(start_fishing, button))

def start_fishing(button):
    changeFishingState(button)
    fishing_loop()


