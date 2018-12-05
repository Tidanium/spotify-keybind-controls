from pykeyboard import PyKeyboard, PyKeyboardEvent
from pymouse import PyMouse, PyMouseEvent
import platform


if platform.system() == "Windows":
    from lib import windows
elif platform.system() == "Linux":
    from lib import linux
