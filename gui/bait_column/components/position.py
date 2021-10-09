from tkinter import Label, LabelFrame, Scale, Entry, HORIZONTAL
from utils.config import dict

def bait_column_position(bait_column):
    bait_column_position_header = Label(bait_column, text = "Bait positions (px)")
    bait_column_position_header.grid(row=0, column=0)
    bait_column_position_container = LabelFrame(bait_column)
    bait_column_position_container.grid(row=1, column=0, padx=(10))

    bait_selection_column_position_x_container = Label(bait_column_position_container, height=1)
    bait_selection_column_position_x_container.grid(row=0, column=0, padx=(20,19))
    bait_selection_column_position_x_text = Label(bait_selection_column_position_x_container, text="X:")
    bait_selection_column_position_x_text.grid(row=0, column=0, pady=(20, 0))
    bait_selection_column_position_x_scale = Scale(bait_selection_column_position_x_container, from_=0, to=dict['resolution']['x'], orient=HORIZONTAL, variable=dict['bait']['bait_x'])
    bait_selection_column_position_x_scale.grid(row=0, column=1)
    bait_selection_column_position_x_entry = Entry(bait_selection_column_position_x_container, width=4, textvariable=dict['bait']['bait_x'])
    bait_selection_column_position_x_entry.grid(row=0, column=2, pady=(20, 0))
    bait_selection_column_position_y_container = Label(bait_column_position_container, height=1)
    bait_selection_column_position_y_container.grid(row=1, column=0)
    bait_selection_column_position_y_text = Label(bait_selection_column_position_y_container, text="Y:")
    bait_selection_column_position_y_text.grid(row=0, column=0, pady=(20, 0))
    bait_selection_column_position_y_scale = Scale(bait_selection_column_position_y_container, from_=0, to=dict['resolution']['y'], orient=HORIZONTAL, variable=dict['bait']['bait_y'])
    bait_selection_column_position_y_scale.grid(row=0, column=1)
    bait_selection_column_position_y_entry = Entry(bait_selection_column_position_y_container, width=4, textvariable=dict['bait']['bait_y'])
    bait_selection_column_position_y_entry.grid(row=0, column=2, pady=(20, 0))
