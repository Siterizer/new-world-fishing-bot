from tkinter import Label, LabelFrame

from gui.repairing_column.components.enable_repairs import repairing_column_enable_repairs
from gui.repairing_column.components.every import repairing_column_every
from gui.repairing_column.components.position import repairing_column_position
from gui.repairing_column.components.show_button import repairing_column_show
from gui.repairing_column.components.move_time import move_time
from gui.repairing_column.components.enable_move import repairing_column_enable_move


def add_repairing_column(app, config):
    repairing_column_header = Label(app, text="Repairing")
    repairing_column_header.grid(row=0, column=1, pady=(3, 0))
    repairing_column = LabelFrame(app)
    repairing_column.grid(row=1, column=1, padx=(10, 0), pady=(0, 50))
    repairing_column_position_header = Label(
        repairing_column, text="Click position (px)"
    )
    repairing_column_position_header.grid(row=0, column=0)

    repairing_column_position(repairing_column, config)
    repairing_column_every(repairing_column, config)
    repairing_column_enable_repairs(app, repairing_column)
    repairing_column_show(app, repairing_column, config)
    move_time(repairing_column, config)
    repairing_column_enable_move(app, repairing_column)
