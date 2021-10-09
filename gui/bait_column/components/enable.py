from tkinter import Label, LabelFrame, Button
from utils.config import dict
from functools import partial
from gui.gui_functions import change_bait_button_state

def bait_column_enable(bait_column):
    bait_column_enable_container = LabelFrame(bait_column)
    bait_column_enable_container.grid(row=4, column=0, pady=(2, 2))
    bait_column_enable_text = Label(bait_column_enable_container, text="Enable bait:")
    bait_column_enable_text.grid(row=0, column=0, padx=(15, 15))
    bait_column_enable_button = Button(bait_column_enable_container)
    change_bait_button_state(bait_column_enable_button)
    change_bait_button_state(bait_column_enable_button)
    bait_column_enable_button.configure(command = partial(change_bait_button_state, bait_column_enable_button))
    bait_column_enable_button.grid(row=0, column=1, padx=(50, 14))
