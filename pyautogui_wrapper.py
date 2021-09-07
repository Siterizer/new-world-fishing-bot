from logging_module import *
import pyautogui

def click_mouse_with_coordinates(x1, y1):
    log("click: x={} y= {}".format(x1, y1))
    pyautogui.click(x=x1, y=y1)

def press_key(key):
    log("press key:{}".format(key))
    pyautogui.keyDown(key)

def release_key(key):
    log("release key:{}".format(key))
    pyautogui.keyUp(key)

def press_mouse_key():
    log("press mouse key")
    pyautogui.mouseDown()

def release_mouse_key():
    log("release mouse key")
    pyautogui.mouseUp()

def get_screenshot(x, y, width, height):
    log("take screenshot: x={} y={} width={} height={}".format(x, y, width, height))
    return pyautogui.screenshot(region=(x, y, width, height))
