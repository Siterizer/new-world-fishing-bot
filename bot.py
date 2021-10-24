import utils.global_variables as gv
from gui.gui_initializer import gui_init
import random
import string

gui_init()
gv.root.iconbitmap(gv.ICON_PATH)
gv.root.title(''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(10)))
gv.root.mainloop()
