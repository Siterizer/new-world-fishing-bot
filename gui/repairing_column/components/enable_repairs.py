from tkinter import Label, LabelFrame, Button
from functools import partial


def repairing_column_enable_repairs(app, repairing_column):
    repairing_column_enable_repairs_container = LabelFrame(repairing_column)
    repairing_column_enable_repairs_container.grid(row=4, column=0, pady=(0, 5))
    repairing_column_enable_repairs_text = Label(repairing_column_enable_repairs_container, text="Enable repairs:")
    repairing_column_enable_repairs_text.grid(row=0, column=0, padx=(0, 37))
    repairing_column_enable_repairs_button = Button(repairing_column_enable_repairs_container)
    app.change_repair_button_state(repairing_column_enable_repairs_button)
    app.change_repair_button_state(repairing_column_enable_repairs_button)
    repairing_column_enable_repairs_button.configure(
        command=partial(app.change_repair_button_state, repairing_column_enable_repairs_button)
    )
    repairing_column_enable_repairs_button.grid(row=0, column=1, padx=(0, 13))
