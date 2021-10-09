from gui.bait_column.components.enable import *
from gui.bait_column.components.position import *
from gui.bait_column.components.equip_position import *
from gui.bait_column.components.show_button import *
import utils.global_variables as gv
from tkinter import Label, LabelFrame

def bait_column():
    bait_column_header = Label(gv.root, text = "Bait")
    bait_column_header.grid(row=0, column=3, pady=(3, 0))
    bait_column = LabelFrame(gv.root)
    bait_column.grid(row=1, column=3, padx=(10, 0), pady=(0, 6))

    bait_column_position(bait_column)
    bait_equip_column_position(bait_column)
    bait_column_enable(bait_column)
    bait_column_show_button(bait_column)