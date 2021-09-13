from tkinter import *
from functools import partial
from resources.config import dict, save_data
from functionality.start_fishing import start_fishing
from global_variables import get_root

def gui_init():
    get_root().resizable(False, False)
    get_root().protocol("WM_DELETE_WINDOW", partial(on_closing))

    fishing_column_header = Label(get_root(), text = "Fishing")
    fishing_column_header.grid(row=0, column=0, pady=(3, 0))
    fishing_column = LabelFrame(get_root())
    fishing_column.grid(row=1, column=0, padx=(10, 0), pady=(0, 5))
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
    fishing_column_attributes_header = Label(fishing_column, text = "Rectangle attributes (px)")
    fishing_column_attributes_header.grid(row=2, column=0)
    fishing_column_attributes_container = LabelFrame(fishing_column)
    fishing_column_attributes_container.grid(row=3, column=0, padx=(10))
    fishing_column_attributes_width_container = Label(fishing_column_attributes_container, height=1)
    fishing_column_attributes_width_container.grid(row=0, column=0, padx=(5))
    fishing_column_attributes_width_text = Label(fishing_column_attributes_width_container, text="Width:")
    fishing_column_attributes_width_text.grid(row=0, column=0, pady=(20, 0))
    fishing_column_attributes_width_scale = Scale(fishing_column_attributes_width_container, from_=0, to=dict['resolution']['x'], orient=HORIZONTAL, variable=dict['fishing']['width'])
    fishing_column_attributes_width_scale.grid(row=0, column=1)
    fishing_column_attributes_width_entry = Entry(fishing_column_attributes_width_container, width=4, textvariable=dict['fishing']['width'])
    fishing_column_attributes_width_entry.grid(row=0, column=2, pady=(20, 0))
    fishing_column_attributes_height_container = Label(fishing_column_attributes_container, height=1)
    fishing_column_attributes_height_container.grid(row=1, column=0, padx=(5))
    fishing_column_attributes_height_text = Label(fishing_column_attributes_height_container, text="Height:")
    fishing_column_attributes_height_text.grid(row=0, column=0, pady=(20, 0))
    fishing_column_attributes_height_scale = Scale(fishing_column_attributes_height_container, from_=0, to=dict['resolution']['y'], orient=HORIZONTAL, variable=dict['fishing']['height'])
    fishing_column_attributes_height_scale.grid(row=0, column=1)
    fishing_column_attributes_height_entry = Entry(fishing_column_attributes_height_container, width=4, textvariable=dict['fishing']['height'])
    fishing_column_attributes_height_entry.grid(row=0, column=2, pady=(20, 0))
    fishing_column_show_container = LabelFrame(fishing_column)
    fishing_column_show_container.grid(row=4, column=0, pady=(5, 0))
    fishing_column_show_button = Button(fishing_column_show_container, text = "Show rectangle")
    fishing_column_show_button.configure(command = partial(popup_rectangle_window, fishing_column_show_button, dict['fishing']['x'], dict['fishing']['y'], dict['fishing']['width'], dict['fishing']['height']))
    fishing_column_show_button.grid(row=4, column=0, padx=(50, 51), pady=(2, 4))

    repairing_column_header = Label(get_root(), text = "Repairing")
    repairing_column_header.grid(row=0, column=1, pady=(3, 0))
    repairing_column = LabelFrame(get_root())
    repairing_column.grid(row=1, column=1, padx=(10, 10), pady=(0, 53))
    repairing_column_position_header = Label(repairing_column, text = "Click position (px)")
    repairing_column_position_header.grid(row=0, column=0)
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
    repairing_column_every_container = LabelFrame(repairing_column)
    repairing_column_every_container.grid(row=3, column=0, pady=(5, 5))
    repairing_column_every_text_left = Label(repairing_column_every_container, text = "Repair every:")
    repairing_column_every_text_left.grid(row=0, column=0, padx=(0, 5))
    repairing_column_every_entry = Entry(repairing_column_every_container, width=4, textvariable=dict['repairing']['every'])
    repairing_column_every_entry.grid(row=0, column=1, padx=(41, 0))
    repairing_column_every_text_right = Label(repairing_column_every_container, text = "s")
    repairing_column_every_text_right.grid(row=0, column=3, padx=(0, 6))
    repairing_column_enable_container = LabelFrame(repairing_column)
    repairing_column_enable_container.grid(row=4, column=0, pady=(0, 5))
    repairing_column_enable_text = Label(repairing_column_enable_container, text="Enable repairs:")
    repairing_column_enable_text.grid(row=0, column=0, padx=(0, 37))
    repairing_column_enable_button = Button(repairing_column_enable_container)
    change_repair_button_state(repairing_column_enable_button)
    change_repair_button_state(repairing_column_enable_button)
    repairing_column_enable_button.configure(command = partial(change_repair_button_state, repairing_column_enable_button))
    repairing_column_enable_button.grid(row=0, column=1, padx=(0, 13))
    repairing_column_show_container = LabelFrame(repairing_column)
    repairing_column_show_container.grid(row=5, column=0, pady=(3, 0))
    repairing_column_show_button = Button(repairing_column_show_container, text = "Show repair position")
    repairing_column_show_button.configure(command = partial(popup_rectangle_window, repairing_column_show_button, dict['repairing']['x'], dict['repairing']['y'], dict['repairing']['length'], dict['repairing']['length']))
    repairing_column_show_button.grid(row=0, column=0, padx=(25, 20), pady=(2, 4))
    start_fishing_container = LabelFrame(get_root())
    start_fishing_container.grid(row=3, columnspan=2, padx=(10, 0), pady=(15, 0))
    start_fishing_button = Button(start_fishing_container, text = "Start fishing", font=18)
    start_fishing_button.configure(command = partial(start_fishing, start_fishing_button))
    start_fishing_button.grid(row=0, column=0)

def popup_rectangle_window(button, x, y, width, height):
    window = Toplevel()
    window.resizable(False, False)
    window.attributes('-fullscreen', True)
    window.wm_attributes('-transparentcolor', window['bg'])
    canvas = Canvas(window, width=10000, height=10000)
    canvas.create_rectangle(x.get(), y.get(), x.get()+width.get(), y.get()+height.get(), fill="green")
    canvas.pack()
    button.configure(command = partial(destroy_rectangle_window, window, button, x, y, width, height))

def destroy_rectangle_window(window, button, x, y, width, height):
    window.destroy()
    button.configure(command = partial(popup_rectangle_window, button, x,y,width,height))

def on_closing():
    save_data()
    get_root().destroy()

def change_repair_button_state(button):
    if (dict['repairing']['enable'].get() == 1):
        button.configure(text="OFF")
        button.configure(bg="red")
        dict['repairing']['enable'] = IntVar(value=0)
    else:
        button.configure(text="ON ")
        button.configure(bg="green")
        dict['repairing']['enable'] = IntVar(value=1)

