from tkinter import LabelFrame, Button

from functools import partial


def fishing_column_show_button(app, fishing_column, config):
    fishing_column_show_container = LabelFrame(fishing_column)
    fishing_column_show_container.grid(row=4, column=0, pady=(5, 0))
    fishing_column_show_button = Button(fishing_column_show_container, text="Show fishing position")
    fishing_column_show_button.configure(
        command=partial(
            app.popup_rectangle_window,
            fishing_column_show_button,
            config["fishing"]["x"],
            config["fishing"]["y"],
            config["fishing"]["width"],
            config["fishing"]["height"],
        )
    )
    fishing_column_show_button.grid(row=4, column=0, padx=(34, 34), pady=(2, 4))
