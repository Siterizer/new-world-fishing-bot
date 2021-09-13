from tkinter import *
from functools import partial
from global_variables import init_variables, get_root

init_variables()

import initializer
initializer.init()

get_root().mainloop()