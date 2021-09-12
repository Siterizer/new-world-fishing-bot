from tkinter import *
from functools import partial
from global_variables import init_variables

init_variables()
root = Tk()
import initializer
root.resizable(False, False)
initializer.init(root)

root.protocol("WM_DELETE_WINDOW", partial(initializer.on_closing, root))
root.mainloop()