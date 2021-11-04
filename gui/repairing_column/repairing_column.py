from tkinter import Label, LabelFrame

from gui.repairing_column.components.enable import repairing_column_enable
from gui.repairing_column.components.every import repairing_column_every
from gui.repairing_column.components.position import repairing_column_position
from gui.repairing_column.components.show_button import repairing_column_show


def add_repairing_column(app, config):
    repairing_column_header = Label(app, text="Repairing")
    repairing_column_header.grid(row=0, column=1, pady=(3, 0))
    repairing_column = LabelFrame(app)
    repairing_column.grid(row=1, column=1, padx=(10, 0), pady=(0, 118))
    repairing_column_position_header = Label(
        repairing_column, text="Click position (px)"
    )
    repairing_column_position_header.grid(row=0, column=0)

    repairing_column_position(repairing_column, config)
    repairing_column_every(repairing_column, config)
    repairing_column_enable(app, repairing_column)
    repairing_column_show(app, repairing_column, config)
