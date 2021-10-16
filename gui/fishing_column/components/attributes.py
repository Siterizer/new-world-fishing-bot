from tkinter import Label, LabelFrame, Scale, Entry, HORIZONTAL
from utils.config import config_dict


def fishing_column_attributes(fishing_column):
    fishing_column_attributes_header = Label(fishing_column, text="Rectangle attributes (px)")
    fishing_column_attributes_header.grid(row=2, column=0)
    fishing_column_attributes_container = LabelFrame(fishing_column)
    fishing_column_attributes_container.grid(row=3, column=0, padx=(10))
    fishing_column_attributes_width_container = Label(fishing_column_attributes_container, height=1)
    fishing_column_attributes_width_container.grid(row=0, column=0, padx=(5))
    fishing_column_attributes_width_text = Label(fishing_column_attributes_width_container, text="Width:")
    fishing_column_attributes_width_text.grid(row=0, column=0, pady=(20, 0))
    fishing_column_attributes_width_scale = Scale(
        fishing_column_attributes_width_container,
        from_=0,
        to=config_dict["resolution"]["x"],
        orient=HORIZONTAL,
        variable=config_dict["fishing"]["width"],
    )
    fishing_column_attributes_width_scale.grid(row=0, column=1)
    fishing_column_attributes_width_entry = Entry(
        fishing_column_attributes_width_container,
        width=4,
        textvariable=config_dict["fishing"]["width"],
    )
    fishing_column_attributes_width_entry.grid(row=0, column=2, pady=(20, 0))
    fishing_column_attributes_height_container = Label(fishing_column_attributes_container, height=1)
    fishing_column_attributes_height_container.grid(row=1, column=0, padx=(5))
    fishing_column_attributes_height_text = Label(fishing_column_attributes_height_container, text="Height:")
    fishing_column_attributes_height_text.grid(row=0, column=0, pady=(20, 0))
    fishing_column_attributes_height_scale = Scale(
        fishing_column_attributes_height_container,
        from_=0,
        to=config_dict["resolution"]["y"],
        orient=HORIZONTAL,
        variable=config_dict["fishing"]["height"],
    )
    fishing_column_attributes_height_scale.grid(row=0, column=1)
    fishing_column_attributes_height_entry = Entry(
        fishing_column_attributes_height_container,
        width=4,
        textvariable=config_dict["fishing"]["height"],
    )
    fishing_column_attributes_height_entry.grid(row=0, column=2, pady=(20, 0))
