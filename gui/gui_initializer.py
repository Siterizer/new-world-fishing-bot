from functools import partial
from gui.gui_functions import start_fishing, on_closing
from gui.fishing_column.fishing_column import fishing_column
from gui.repairing_column.repairing_column import repairing_column
from gui.bait_column.bait_column import bait_column
from gui.start_fishing_button.start_fishing_button import start_fishing_button
import utils.global_variables as gv

def gui_init():
    gv.root.resizable(False, False)
    gv.root.protocol("WM_DELETE_WINDOW", partial(on_closing))
    fishing_column()
    repairing_column()
    bait_column()
    start_fishing_button()
