import asyncio
import logging
import random
import string
import threading
import tkinter as tk
from functools import partial

from functionality.fishing_loop import fishing_loop
from gui.bait_column.bait_column import add_bait_column
from gui.fishing_column.fishing_column import add_fishing_column
from gui.repairing_column.repairing_column import add_repairing_column
from gui.start_fishing_button.start_fishing_button import add_start_fishing_button
from utils.config import get_config, save_data
from utils.global_variables import ICON_PATH
from wrappers.logging_wrapper import log_level


class FishingBoi(tk.Tk):
    def __init__(self):
        super().__init__()

        self.resizable(False, False)
        self.protocol("WM_DELETE_WINDOW", partial(self.on_closing))
        self.iconbitmap(ICON_PATH)
        self.title("".join(random.choice(string.ascii_uppercase + string.digits) for _ in range(10)))

        self.continue_fishing = False
        self.fishing_coro = None
        self.asyncio_event_loop = asyncio.get_event_loop()

        self.config = get_config()

        print(self.config["log_lvl"])
        logging.getLogger().setLevel(log_level.get(self.config["log_lvl"], "INFO"))

        add_fishing_column(self, self.config)
        add_repairing_column(self, self.config)
        add_bait_column(self, self.config)
        add_start_fishing_button(self)

        # self.asyncio_event_loop.set_debug(True)
        threading.Thread(daemon=True, target=self.asyncio_event_loop.run_forever).start()

    def popup_rectangle_window(self, button, x, y, width, height):
        window = tk.Toplevel()
        window.resizable(False, False)
        window.attributes("-fullscreen", True)
        window.wm_attributes("-transparentcolor", window["bg"])
        window.attributes('-topmost',True)
        canvas = tk.Canvas(window, width=10000, height=10000)
        canvas.create_rectangle(
            x.get(),
            y.get(),
            x.get() + width.get(),
            y.get() + height.get(),
            outline="green",
            width=5,
        )
        canvas.pack()
        button.configure(command=partial(self.destroy_rectangle_window, window, button, x, y, width, height))

    def destroy_rectangle_window(self, window, button, x, y, width, height):
        window.destroy()
        button.configure(command=partial(self.popup_rectangle_window, button, x, y, width, height))

    def on_closing(self):
        save_data(self.config)
        self.destroy()

    def change_repair_button_state(self, button):
        if self.config["repairing"]["enable"].get() == 1:
            button.configure(text="OFF")
            button.configure(bg="red")
            self.config["repairing"]["enable"] = tk.IntVar(value=0)
        else:
            button.configure(text="ON ")
            button.configure(bg="green")
            self.config["repairing"]["enable"] = tk.IntVar(value=1)

    def change_bait_button_state(self, button):
        if self.config["bait"]["enable"].get() == 1:
            button.configure(text="OFF")
            button.configure(bg="red")
            self.config["bait"]["enable"] = tk.IntVar(value=0)
        else:
            button.configure(text="ON ")
            button.configure(bg="green")
            self.config["bait"]["enable"] = tk.IntVar(value=1)

    def changeFishingState(self, button):
        self.continue_fishing = not self.continue_fishing
        if self.continue_fishing:
            button.configure(text="Stop fishing")
            button.configure(command=partial(self.changeFishingState, button))
            return
        button.configure(text="Start fishing")

        try:
            task = [task for task in asyncio.all_tasks(self.asyncio_event_loop) if task.get_name() == "fishing_loop"]
            if task:
                task = task.pop()
                self.asyncio_event_loop.call_soon_threadsafe(task.cancel)
        except asyncio.CancelledError:
            pass

        button.configure(command=partial(self.start_fishing, button))

    def start_fishing(self, button):
        self.changeFishingState(button)
        self.fishing_coro = self.asyncio_event_loop.call_soon_threadsafe(self.do_create_task)

    def do_create_task(self):
        self.asyncio_event_loop.create_task(fishing_loop(self.config), name="fishing_loop")


if __name__ == "__main__":
    app = FishingBoi()
    app.mainloop()
