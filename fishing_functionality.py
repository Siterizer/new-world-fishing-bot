from config import dict
from tkinter import *
import pyautogui
import time


def start_fishing(button):
    print ('siema')
    button.configure(text = "Stop fishing")
    repair()

def repair():
    pyautogui.keyDown('tab') #Open equipment
    pyautogui.keyUp('tab') #release key
    time.sleep(2) #Wait equipment loads
    pyautogui.keyDown('r') #Press repair hotkey
    pyautogui.click(x=dict['repairing']['x'].get(), y=dict['repairing']['y'].get()) #Repair rod
    time.sleep(2) #Wait 2s until the rod is finished repairing
    pyautogui.keyUp('r') #release key
    pyautogui.keyDown('escape') #escape equipment
    pyautogui.keyUp('escape') #release key
