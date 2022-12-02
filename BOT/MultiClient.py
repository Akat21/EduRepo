import os
import subprocess
from ahk import AHK
import pygetwindow
from SoPNv_Farm_bot import *

def Check_if_In_Logging_Screen():
    box = (819,366,1090,379)
    img = ImageGrab.grab(box)
    greyimg = ImageOps.grayscale(img)
    g = np.array(greyimg.getcolors())
    return g.sum()

def Check_if_In_Character_Choose_Screen():
    box = (860,973,1055,1027)
    img = ImageGrab.grab(box)
    greyimg = ImageOps.grayscale(img)
    g = np.array(greyimg.getcolors())
    return g.sum()

def open_Nostale(slot):
    ahk =AHK()
    subprocess.call([r"C:\Program Files (x86)\GameforgeClient\Nostale\Nostale.exe"])
    win = ahk.find_window(title = b'Gameforge Client')
    win.activate()
    time.sleep(1)
    ahk.click(400,569)
    time.sleep(1)
    if slot == 1:
        ahk.click(799,525)
    elif slot == 2:
        ahk.click(799,575)
    ahk.click(1499,160)
    while(True):
        if Check_if_In_Logging_Screen() == 18490:
            time.sleep(0.5)
            ahk.click(950,412)
            time.sleep(0.5)
            ahk.click(1215,577)
            while (True):
                if Check_if_In_Character_Choose_Screen() == 40678:
                    time.sleep(0.5)
                    ahk.double_click(561,73)
                    break
            break
