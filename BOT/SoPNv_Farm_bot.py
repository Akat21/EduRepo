from PIL import ImageGrab, ImageOps
import time
import pyautogui
import numpy as np
import keyboard

def Check_if_Killed():
    box = (853,11,910,21)
    img = ImageGrab.grab(box)
    greyimg = ImageOps.grayscale(img)
    g = np.array(greyimg.getcolors())
    return g.sum()

def Check_if_chat_on():
    box = (9,1020,23,1032)
    img = ImageGrab.grab(box)
    greyimg = ImageOps.grayscale(img)
    g = np.array(greyimg.getcolors())
    return g.sum()

def Check_if_low_hp():
    box = (147,38,183,45)
    img = ImageGrab.grab(box)
    greyimg = ImageOps.grayscale(img)
    g = np.array(greyimg.getcolors())
    return g.sum()

def Auto_Attack_and_Pick_up():
    if Check_if_Killed() > 4000 and Check_if_chat_on() != 10542:
        for i in range(5):
            pyautogui.press('x')
            time.sleep(0.2)
        for i in range(3):
            pyautogui.press('space')

