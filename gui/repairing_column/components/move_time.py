from tkinter import Label, LabelFrame, Entry


def move_time(repairing_column, config):
    repairing_column_move_time = LabelFrame(repairing_column)
    repairing_column_move_time.grid(row=6, column=0, pady=(5, 5))
    repairing_column_move_time_text_left = Label(repairing_column_move_time, text="Move timeout:")
    repairing_column_move_time_text_left.grid(row=0, column=0, padx=(0, 1))
    repairing_column_move_time_min_entry = Entry(
        repairing_column_move_time,
        width=4,
        textvariable=config["repairing"]["timeouts"]["move_around"]["min"],
    )
    repairing_column_move_time_min_entry.grid(row=0, column=1, padx=(1, 0))
    repairing_column_move_time_text_middle = Label(repairing_column_move_time, text="-")
    repairing_column_move_time_text_middle.grid(row=0, column=2, padx=(0, 0))
    repairing_column_move_time_max_entry = Entry(
        repairing_column_move_time,
        width=4,
        textvariable=config["repairing"]["timeouts"]["move_around"]["max"],
    )
    repairing_column_move_time_max_entry.grid(row=0, column=3, padx=(0, 0))
    repairing_column_move_time_text_right = Label(repairing_column_move_time, text="s")
    repairing_column_move_time_text_right.grid(row=0, column=4, padx=(0, 0))
