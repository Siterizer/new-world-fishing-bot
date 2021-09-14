from tkinter import Label, LabelFrame, Scale, Entry, HORIZONTAL
from utils.config import dict

def fishing_column_position(fishing_column):
    fishing_column_position_header = Label(fishing_column, text = "Rectangle position (px)")
    fishing_column_position_header.grid(row=0, column=0)
    fishing_column_position_container = LabelFrame(fishing_column)
    fishing_column_position_container.grid(row=1, column=0, padx=(10))
    fishing_column_position_x_container = Label(fishing_column_position_container, height=1)
    fishing_column_position_x_container.grid(row=0, column=0, padx=(20,19))
    fishing_column_position_x_text = Label(fishing_column_position_x_container, text="X:")
    fishing_column_position_x_text.grid(row=0, column=0, pady=(20, 0))
    fishing_column_position_x_scale = Scale(fishing_column_position_x_container, from_=0, to=dict['resolution']['x'], orient=HORIZONTAL, variable=dict['fishing']['x'])
    fishing_column_position_x_scale.grid(row=0, column=1)
    fishing_column_position_x_entry = Entry(fishing_column_position_x_container, width=4, textvariable=dict['fishing']['x'])
    fishing_column_position_x_entry.grid(row=0, column=2, pady=(20, 0))
    fishing_column_position_y_container = Label(fishing_column_position_container, height=1)
    fishing_column_position_y_container.grid(row=1, column=0)
    fishing_column_position_y_text = Label(fishing_column_position_y_container, text="Y:")
    fishing_column_position_y_text.grid(row=0, column=0, pady=(20, 0))
    fishing_column_position_y_scale = Scale(fishing_column_position_y_container, from_=0, to=dict['resolution']['y'], orient=HORIZONTAL, variable=dict['fishing']['y'])
    fishing_column_position_y_scale.grid(row=0, column=1)
    fishing_column_position_y_entry = Entry(fishing_column_position_y_container, width=4, textvariable=dict['fishing']['y'])
    fishing_column_position_y_entry.grid(row=0, column=2, pady=(20, 0))
