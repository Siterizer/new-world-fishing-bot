from tkinter import Label, LabelFrame, Entry, Scale, HORIZONTAL
from utils.config import dict

def repairing_column_position(repairing_column):
    repairing_column_position_container = LabelFrame(repairing_column)
    repairing_column_position_container.grid(row=1, column=0, padx=(10))
    repairing_column_position_x_container = Label(repairing_column_position_container, height=1)
    repairing_column_position_x_container.grid(row=0, column=0, padx=(5))
    repairing_column_position_x_text = Label(repairing_column_position_x_container, text="X:", anchor="s")
    repairing_column_position_x_text.grid(row=0, column=0, pady=(20, 0))
    repairing_column_position_x_scale = Scale(repairing_column_position_x_container, from_=0, to=dict['resolution']['x'], orient=HORIZONTAL, variable=dict['repairing']['x'])
    repairing_column_position_x_scale.grid(row=0, column=1)
    repairing_column_position_x_entry = Entry(repairing_column_position_x_container, width=4, textvariable=dict['repairing']['x'])
    repairing_column_position_x_entry.grid(row=0, column=2, pady=(20, 0))
    repairing_column_position_y_container = Label(repairing_column_position_container, height=1)
    repairing_column_position_y_container.grid(row=1, column=0)
    repairing_column_position_y_text = Label(repairing_column_position_y_container, text="Y:")
    repairing_column_position_y_text.grid(row=0, column=0, pady=(20, 0))
    repairing_column_position_y_scale = Scale(repairing_column_position_y_container, from_=0, to=dict['resolution']['y'], orient=HORIZONTAL, variable=dict['repairing']['y'])
    repairing_column_position_y_scale.grid(row=0, column=1)
    repairing_column_position_y_entry = Entry(repairing_column_position_y_container, width=4, textvariable=dict['repairing']['y'])
    repairing_column_position_y_entry.grid(row=0, column=2, pady=(20, 0))
