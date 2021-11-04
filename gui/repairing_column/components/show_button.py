from tkinter import LabelFrame, Button
from functools import partial


def repairing_column_show(app, repairing_column, config):
    repairing_column_show_container = LabelFrame(repairing_column)
    repairing_column_show_container.grid(row=5, column=0, pady=(3, 0))
    repairing_column_show_button = Button(repairing_column_show_container, text="Show repair position")
    repairing_column_show_button.configure(
        command=partial(
            app.popup_rectangle_window,
            repairing_column_show_button,
            config["repairing"]["x"],
            config["repairing"]["y"],
            config["repairing"]["length"],
            config["repairing"]["length"],
        )
    )
    repairing_column_show_button.grid(row=0, column=0, padx=(25, 20), pady=(2, 4))
