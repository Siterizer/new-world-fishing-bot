from PIL.Image import NEAREST
from utils.global_variables import SCREENSHOTS_PATH
import pyautogui
from time import sleep
from datetime import datetime


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

def get_screenshot(x, y, width, height):
    screenshot = pyautogui.screenshot(region=(x, y, width, height))
    screenshot = screenshot.resize((224, 224), NEAREST)
    return screenshot

def save_screenshot(screenshot):
    actual_time = datetime.utcnow().strftime('%Y_%m_%d_%H_%M_%S_%f')
    file_name = actual_time + ".jpg"
    screenshot.save(SCREENSHOTS_PATH+ file_name)
