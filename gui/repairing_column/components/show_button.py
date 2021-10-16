from tkinter import LabelFrame, Button
from utils.config import config_dict
from functools import partial
from gui.gui_functions import popup_rectangle_window


def repairing_column_show(repairing_column):
    repairing_column_show_container = LabelFrame(repairing_column)
    repairing_column_show_container.grid(row=5, column=0, pady=(3, 0))
    repairing_column_show_button = Button(repairing_column_show_container, text="Show repair position")
    repairing_column_show_button.configure(
        command=partial(
            popup_rectangle_window,
            repairing_column_show_button,
            config_dict["repairing"]["x"],
            config_dict["repairing"]["y"],
            config_dict["repairing"]["length"],
            config_dict["repairing"]["length"],
        )
    )
    repairing_column_show_button.grid(row=0, column=0, padx=(25, 20), pady=(2, 4))
