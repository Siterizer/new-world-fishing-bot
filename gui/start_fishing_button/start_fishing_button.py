import utils.global_variables as gv
import utils.global_variables as gv
import keyboard
from tkinter import Button, LabelFrame
from functools import partial
from gui.gui_functions import start_fishing_button_pressed, stop_fishing_button_pressed


def start_fishing_button():
    start_fishing_container = LabelFrame(gv.root)
    start_fishing_container.grid(row=6, columnspan=4, padx=(10, 0), pady=(15, 0))
    start_fishing_button = Button(start_fishing_container, text = "Start fishing", font=18, bg="green", fg="white")
    start_fishing_button.configure(command = partial(start_fishing_button_pressed, start_fishing_button))

    # start a thread to listen for hotkey 0 to pause/resume the bot
    keyboard.add_hotkey('0', partial(stop_fishing_button_pressed, start_fishing_button))
    keyboard.add_hotkey('9', partial(start_fishing_button_pressed, start_fishing_button))

    start_fishing_button.grid(row=0, column=0)
