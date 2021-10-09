from tkinter import LabelFrame, Button
from utils.config import dict
from functools import partial
from gui.gui_functions import popup_rectangle_window

def bait_column_show_button(bait_column):
    bait_column_show_container = LabelFrame(bait_column)
    bait_column_show_container.grid(row=5, column=0, pady=(3, 0))
    bait_column_show_button = Button(bait_column_show_container, text = "Show bait position")
    bait_column_show_button.configure(command = partial(popup_rectangle_window, bait_column_show_button, dict['bait']['bait_x'], dict['bait']['bait_y'], dict['bait']['length'], dict['bait']['length']))
    bait_column_show_button.grid(row=0, column=0, padx=(25, 20), pady=(2, 4))

    bait_equip_column_show_button = Button(bait_column_show_container, text = "Show equip button position")
    bait_equip_column_show_button.configure(command = partial(popup_rectangle_window, bait_equip_column_show_button, dict['bait']['equip_button_x'], dict['bait']['equip_button_y'], dict['bait']['length'], dict['bait']['length']))
    bait_equip_column_show_button.grid(row=1, column=0, padx=(17, 18), pady=(2, 4))