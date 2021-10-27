from tkinter import Label, LabelFrame

from gui.fishing_column.components.attributes import fishing_column_attributes
from gui.fishing_column.components.position import fishing_column_position
from gui.fishing_column.components.show_button import fishing_column_show_button


def add_fishing_column(app, config):
    fishing_column_header = Label(app, text="Fishing")
    fishing_column_header.grid(row=0, column=0, pady=(3, 0))
    fishing_column = LabelFrame(app)
    fishing_column.grid(row=1, column=0, padx=(10, 0), pady=(0, 70))

    fishing_column_position(fishing_column, config)
    fishing_column_attributes(fishing_column, config)
    fishing_column_show_button(app, fishing_column, config)
