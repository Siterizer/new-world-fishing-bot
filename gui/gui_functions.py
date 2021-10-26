from tkinter import Toplevel, Canvas, IntVar
from functools import partial
from utils.config import dict, save_data
from functionality.fishing_loop import fishing_loop
from wrappers.logging_wrapper import info, debug
from wrappers.win32api_wrapper import *
from utils.config import dict, random_timeout
import utils.global_variables as gv
import keyboard
import threading

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

def change_bait_button_state(button):
    if (dict['bait']['enable'].get() == 1):
        button.configure(text="OFF")
        button.configure(bg="red")
        dict['bait']['enable'] = IntVar(value=0)
    else:
        button.configure(text="ON ")
        button.configure(bg="green")
        dict['bait']['enable'] = IntVar(value=1)

def stop_fishing_button_pressed(button):
    # prevent button being pressed twice
    if (not gv.continue_fishing):
        info("Skipping because already pressed stop button")
        return
    info("Stop button pressed")
    gv.continue_fishing = False
    event = threading.Event()
    event.set()
    button.configure(text="Start fishing")
    button.configure(command=partial(start_fishing_button_pressed, button))

def start_fishing_button_pressed(button):
    # prevent button being pressed twice
    if (gv.continue_fishing):
        info("Skipping because already pressed start button")
        return
    info("Start button pressed")
    gv.continue_fishing = True
    button.configure(text="Stop fishing")
    button.configure(command=partial(stop_fishing_button_pressed, button))
    #threading.Thread(target=fake_loop).start()
    event = threading.Event()
    threading.Thread(target=fishing_loop, args=(event,)).start()

def fake_loop():
    if (not gv.continue_fishing):
        info('stopping loop')
        return
    info('starting new loop')
    if (gv.continue_fishing):
        gv.root.after(int(random_timeout(dict['fishing']['timeouts']['loop'])*1000), fake_loop)