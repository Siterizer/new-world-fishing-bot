from tkinter import Label, LabelFrame, Scale, Entry, HORIZONTAL
from utils.config import dict

def bait_equip_column_position(bait_column):
    bait_column_position_header = Label(bait_column, text = "Bait equip button positions (px)")
    bait_column_position_header.grid(row=2, column=0)
    bait_column_position_container = LabelFrame(bait_column)
    bait_column_position_container.grid(row=3, column=0, padx=(10))

    bait_equip_button_column_position_x_container = Label(bait_column_position_container, height=1)
    bait_equip_button_column_position_x_container.grid(row=0, column=0, padx=(20,19))
    bait_equip_button_column_position_x_text = Label(bait_equip_button_column_position_x_container, text="X:")
    bait_equip_button_column_position_x_text.grid(row=0, column=0, pady=(20, 0))
    bait_equip_button_column_position_x_scale = Scale(bait_equip_button_column_position_x_container, from_=0, to=dict['resolution']['x'], orient=HORIZONTAL, variable=dict['bait']['equip_button_x'])
    bait_equip_button_column_position_x_scale.grid(row=0, column=1)
    bait_equip_button_column_position_x_entry = Entry(bait_equip_button_column_position_x_container, width=4, textvariable=dict['bait']['equip_button_x'])
    bait_equip_button_column_position_x_entry.grid(row=0, column=2, pady=(20, 0))
    bait_equip_button_column_position_y_container = Label(bait_column_position_container, height=1)
    bait_equip_button_column_position_y_container.grid(row=1, column=0)
    bait_equip_button_column_position_y_text = Label(bait_equip_button_column_position_y_container, text="Y:")
    bait_equip_button_column_position_y_text.grid(row=0, column=0, pady=(20, 0))
    bait_equip_button_column_position_y_scale = Scale(bait_equip_button_column_position_y_container, from_=0, to=dict['resolution']['y'], orient=HORIZONTAL, variable=dict['bait']['equip_button_y'])
    bait_equip_button_column_position_y_scale.grid(row=0, column=1)
    bait_equip_button_column_position_y_entry = Entry(bait_equip_button_column_position_y_container, width=4, textvariable=dict['bait']['equip_button_y'])
    bait_equip_button_column_position_y_entry.grid(row=0, column=2, pady=(20, 0))