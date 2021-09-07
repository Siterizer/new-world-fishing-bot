import pyautogui

def click_mouse_with_coordinates(x1, y1):
    pyautogui.click(x=x1, y=y1)

def press_key(key):
    pyautogui.keyDown(key)

def release_key(key):
    pyautogui.keyUp(key)

def press_mouse_key():
    pyautogui.mouseDown()

def release_mouse_key():
    pyautogui.mouseUp()

def get_screen_shot(x, y, width, height):
    pyautogui.screenshot(region=(x, y, width, height))
