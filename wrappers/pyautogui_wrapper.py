from PIL import Image
from utils.global_variables import SCREENSHOTS_PATH
import pyautogui
import time
import random
import datetime


def click_mouse_with_coordinates(x1, y1, delay):
    pyautogui.moveTo(x1, y1)
    time.sleep(delay)
    pyautogui.click()

def press_key(key):
    pyautogui.keyDown(key)

def release_key(key):
    pyautogui.keyUp(key)

def press_mouse_key():
    pyautogui.mouseDown()

def release_mouse_key():
    pyautogui.mouseUp()

def get_screenshot(x, y, width, height):
    screenshot = pyautogui.screenshot(region=(x, y, width, height))
    screenshot = screenshot.resize((224, 224), Image.NEAREST)
    return screenshot

def save_screenshot(screenshot):
    actual_time = datetime.datetime.utcnow().strftime('%Y_%m_%d_%H_%M_%S_%f')
    file_name = actual_time + ".jpg"
    screenshot.save(SCREENSHOTS_PATH+ file_name)
