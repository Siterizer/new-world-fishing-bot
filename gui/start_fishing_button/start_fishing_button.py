from tkinter import Button, LabelFrame
from functools import partial


def add_start_fishing_button(app):
    start_fishing_container = LabelFrame(app)
    start_fishing_container.grid(row=3, columnspan=4, padx=(10, 0), pady=(15, 0))
    start_fishing_button = Button(
        start_fishing_container, text="Start fishing", font=18, bg="green", fg="white"
    )
    start_fishing_button.configure(command=partial(app.start_fishing, start_fishing_button))
    start_fishing_button.grid(row=0, column=0)
