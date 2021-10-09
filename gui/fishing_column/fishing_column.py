from gui.fishing_column.components.attributes import *
from gui.fishing_column.components.position import *
from gui.fishing_column.components.show_button import *
import utils.global_variables as gv
from tkinter import Label, LabelFrame

def fishing_column():
    fishing_column_header = Label(gv.root, text = "Fishing")
    fishing_column_header.grid(row=0, column=0, pady=(3, 0))
    fishing_column = LabelFrame(gv.root)
    fishing_column.grid(row=1, column=0, padx=(10, 0), pady=(0, 70))

    fishing_column_position(fishing_column)
    fishing_column_attributes(fishing_column)
    fishing_column_show_button(fishing_column)