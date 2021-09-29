import win32api, win32con
from time import sleep


def click_mouse_with_coordinates(x, y):
    win32api.SetCursorPos((x, y))
    sleep(0.02)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    sleep(0.05)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)

VK_CODE = {'tab':0x09,
           'b':0x42,
           'e':0x45,
           'r':0x52,
           'F3':0x72}

def press_key(key):
    win32api.keybd_event(VK_CODE[key], 0,0,0)
    sleep(.05)

def release_key(key):
    win32api.keybd_event(VK_CODE[key],0 ,win32con.KEYEVENTF_KEYUP ,0)

def press_mouse_key():
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)

def release_mouse_key():
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)