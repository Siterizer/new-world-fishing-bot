from tkinter import LabelFrame, Button
from utils.config import config_dict
from functools import partial
from gui.gui_functions import popup_rectangle_window


def fishing_column_show_button(fishing_column):
    fishing_column_show_container = LabelFrame(fishing_column)
    fishing_column_show_container.grid(row=4, column=0, pady=(5, 0))
    fishing_column_show_button = Button(fishing_column_show_container, text="Show fishing position")
    fishing_column_show_button.configure(
        command=partial(
            popup_rectangle_window,
            fishing_column_show_button,
            config_dict["fishing"]["x"],
            config_dict["fishing"]["y"],
            config_dict["fishing"]["width"],
            config_dict["fishing"]["height"],
        )
    )
    fishing_column_show_button.grid(row=4, column=0, padx=(34, 34), pady=(2, 4))
