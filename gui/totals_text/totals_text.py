import utils.global_variables as gv
import utils.global_variables as gv
import keyboard
from tkinter import Label, LabelFrame
from functools import partial

global totals_text_label

def totals_text():
    gv.minutes_text_label.grid(row=2, column=1, pady=(3, 0))
    gv.casts_text_label.grid(row=3, column=1, pady=(3, 0))
    gv.found_text_label.grid(row=4, column=1, pady=(3, 0))
    gv.caught_text_label.grid(row=5, column=1, pady=(3, 0))
