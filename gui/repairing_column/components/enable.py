from tkinter import Label, LabelFrame, Button
from functools import partial


def repairing_column_enable(app, repairing_column):
    repairing_column_enable_container = LabelFrame(repairing_column)
    repairing_column_enable_container.grid(row=4, column=0, pady=(0, 5))
    repairing_column_enable_text = Label(repairing_column_enable_container, text="Enable repairs:")
    repairing_column_enable_text.grid(row=0, column=0, padx=(0, 37))
    repairing_column_enable_button = Button(repairing_column_enable_container)
    app.change_repair_button_state(repairing_column_enable_button)
    app.change_repair_button_state(repairing_column_enable_button)
    repairing_column_enable_button.configure(
        command=partial(app.change_repair_button_state, repairing_column_enable_button)
    )
    repairing_column_enable_button.grid(row=0, column=1, padx=(0, 13))
