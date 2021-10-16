import utils.global_variables as gv
from gui.gui_initializer import gui_init

gui_init()
gv.root.iconbitmap(gv.ICON_PATH)
gv.root.title("fishing bot")
gv.root.mainloop()
