from tkinter import Label, LabelFrame, Entry


def repairing_column_every(repairing_column, config):
    repairing_column_every_container = LabelFrame(repairing_column)
    repairing_column_every_container.grid(row=3, column=0, pady=(5, 5))
    repairing_column_every_text_left = Label(repairing_column_every_container, text="Repair every:")
    repairing_column_every_text_left.grid(row=0, column=0, padx=(0, 5))
    repairing_column_every_entry = Entry(
        repairing_column_every_container,
        width=4,
        textvariable=config["repairing"]["every"],
    )
    repairing_column_every_entry.grid(row=0, column=1, padx=(41, 0))
    repairing_column_every_text_right = Label(repairing_column_every_container, text="s")
    repairing_column_every_text_right.grid(row=0, column=3, padx=(0, 6))
