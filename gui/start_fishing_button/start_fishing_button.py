import utils.global_variables as gv
import utils.global_variables as gv
from tkinter import Button, LabelFrame
from functools import partial
from gui.gui_functions import start_fishing


def start_fishing_button():
    start_fishing_container = LabelFrame(gv.root)
    start_fishing_container.grid(row=3, columnspan=4, padx=(10, 0), pady=(15, 0))
    start_fishing_button = Button(start_fishing_container, text = "Start fishing", font=18)
    start_fishing_button.configure(command = partial(start_fishing, start_fishing_button))
    start_fishing_button.grid(row=0, column=0)
