from tkinter import Label, LabelFrame

from gui.bait_column.components.enable import bait_column_enable
from gui.bait_column.components.equip_position import bait_equip_column_position
from gui.bait_column.components.position import bait_column_position
from gui.bait_column.components.show_button import bait_column_show_button


def add_bait_column(app, config):
    bait_column_header = Label(app, text="Bait")
    bait_column_header.grid(row=0, column=3, pady=(3, 0))
    bait_column = LabelFrame(app)
    bait_column.grid(row=1, column=3, padx=(10, 0), pady=(0, 6))

    bait_column_position(bait_column, config)
    bait_equip_column_position(bait_column, config)
    bait_column_enable(app, bait_column)
    bait_column_show_button(app, bait_column, config)
