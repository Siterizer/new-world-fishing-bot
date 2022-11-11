from tkinter import Label, LabelFrame, Button
from functools import partial


def repairing_column_enable_move(app, repairing_column):
    repairing_column_enable_move_container = LabelFrame(repairing_column)
    repairing_column_enable_move_container.grid(row=7, column=0, pady=(0, 5))
    repairing_column_enable_move_text = Label(repairing_column_enable_move_container, text="Enable move:")
    repairing_column_enable_move_text.grid(row=0, column=0, padx=(0, 37))
    repairing_column_enable_move_button = Button(repairing_column_enable_move_container)
    app.change_move_around_button_state(repairing_column_enable_move_button)
    app.change_move_around_button_state(repairing_column_enable_move_button)
    repairing_column_enable_move_button.configure(
        command=partial(app.change_move_around_button_state, repairing_column_enable_move_button)
    )
    repairing_column_enable_move_button.grid(row=0, column=1, padx=(0, 13))
