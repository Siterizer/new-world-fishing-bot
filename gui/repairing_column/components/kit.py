from tkinter import Label, LabelFrame, Button
from utils.config import dict
from functools import partial
from gui.gui_functions import change_repair_kit_state

def repairing_column_kit(repairing_column):
    repairing_column_enable_container = LabelFrame(repairing_column)
    repairing_column_enable_container.grid(row=5, column=0, pady=(0, 5))
    repairing_column_enable_text = Label(repairing_column_enable_container, text="Use repair kit:")
    repairing_column_enable_text.grid(row=0, column=0, padx=(0, 37))
    repairing_column_enable_button = Button(repairing_column_enable_container)
    change_repair_kit_state(repairing_column_enable_button)
    change_repair_kit_state(repairing_column_enable_button)
    repairing_column_enable_button.configure(command = partial(change_repair_kit_state, repairing_column_enable_button))
    repairing_column_enable_button.grid(row=0, column=1, padx=(0, 13))
