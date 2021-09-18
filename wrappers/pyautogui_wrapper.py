import pyautogui
from time import sleep


def click_mouse_with_coordinates(x1, y1):
    pyautogui.moveTo(x1, y1)
    sleep(0.05)
    pyautogui.click()

def press_key(key):
    pyautogui.keyDown(key)

def release_key(key):
    pyautogui.keyUp(key)

def press_mouse_key():
    pyautogui.mouseDown()

def release_mouse_key():
    pyautogui.mouseUp()