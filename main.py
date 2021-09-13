from tkinter import *
from functools import partial
from global_variables import init_variables, get_root

init_variables()

from gui_initializer import gui_init
gui_init()

get_root().mainloop()