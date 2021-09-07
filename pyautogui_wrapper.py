from logging_module import *
from PIL import Image
import pyautogui
import win32gui
import win32ui
import win32con
import os

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
    actual_time = datetime.utcnow().strftime('%Y_%m_%d_%H_%M_%S_%f')
    bmpfilenamename = 'saved_data/screenshots/result.bmp'
    #result = 'saved_data/screenshots/' + actual_time + '.jpg'
    result = 'saved_data/screenshots/result.jpg'
    hwnd = win32gui.FindWindow(None, 'tak')
    wDC = win32gui.GetWindowDC(hwnd)
    dcObj=win32ui.CreateDCFromHandle(wDC)
    cDC=dcObj.CreateCompatibleDC()
    dataBitMap = win32ui.CreateBitmap()
    dataBitMap.CreateCompatibleBitmap(dcObj, width, height)
    cDC.SelectObject(dataBitMap)
    cDC.BitBlt((0,0),(width, height) , dcObj, (x,y), win32con.SRCCOPY)
    dataBitMap.SaveBitmapFile(cDC, bmpfilenamename)

    image = Image.open(bmpfilenamename)
    image = image.resize((224*2, 224*2), Image.NEAREST)
    image.save(result)
    dcObj.DeleteDC()
    cDC.DeleteDC()
    os.remove(bmpfilenamename)
    win32gui.ReleaseDC(hwnd, wDC)
    win32gui.DeleteObject(dataBitMap.GetHandle())
    #return pyautogui.screenshot(region=(x, y, width, height))
    return result
