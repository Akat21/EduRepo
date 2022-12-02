from SoPNv_Farm_bot import *


def Check_if_Killed():
    box = (1038,36,1052,47)
    img = ImageGrab.grab(box)
    greyimg = ImageOps.grayscale(img)
    g = np.array(greyimg.getcolors())
    return g.sum()

def Check_if_Boss():
    box = (1014,36,1028,49)
    img = ImageGrab.grab(box)
    greyimg = ImageOps.grayscale(img)
    g = np.array(greyimg.getcolors())
    return g.sum()

def Check_if_Heal():
    box = (263,38,275,46)
    img = ImageGrab.grab(box)
    greyimg = ImageOps.grayscale(img)
    g = np.array(greyimg.getcolors())
    return g.sum()

def Check_if_Full():
    box = (289,38,297,48)
    img = ImageGrab.grab(box)
    greyimg = ImageOps.grayscale(img)
    g = np.array(greyimg.getcolors())
    return g.sum()

def Check_if_CP():
    box = (884,746,905,768)
    img = ImageGrab.grab(box)
    greyimg = ImageOps.grayscale(img)
    g = np.array(greyimg.getcolors())
    return g.sum()

def Check_if_Pet():
    box = (1016,38,1027,48)
    img = ImageGrab.grab(box)
    greyimg = ImageOps.grayscale(img)
    g = np.array(greyimg.getcolors())
    return g.sum()

def AutoAttack():
    pyautogui.press('space')
    time.sleep(0.2)

def Target():
    pyautogui.press('space')
    if Check_if_Boss() == 17666:
        pyautogui.press('esc')
        time.sleep(0.2)
    
def Change_dir_Box(coo):
    box = (coo[0]-120,coo[1]-80,coo[0]+120,coo[1]+80)
    img = ImageGrab.grab(box)
    greyimg = ImageOps.grayscale(img)
    g = np.array(greyimg.getcolors())
    return g.sum()

def Move(dir):
    if dir == "up":
        dir = (990,330)
    elif dir == "left":
        dir = (570,520)
    elif dir == "right":
        dir = (1340,682)
    elif dir == "down":
        dir=(940,786)
    pyautogui.click(dir) 
    if Change_dir_Box(dir) > 71000 and dir == (990,330):
        dir = "left"
    elif Change_dir_Box(dir) < 40000 and dir == (990,330):
        dir = "right"
    elif Change_dir_Box(dir) < 39300 and dir == (1340,682):
        dir = "down"
    elif Change_dir_Box(dir) < 38500 and dir == (940,786):
        dir = "left"
    elif Change_dir_Box(dir) < 38700 and dir != (940, 786):
        dir = "up"
    return dir

def Heal(bind):
    if Check_if_Heal() != 6278:
        pyautogui.press(bind)

def Back(cnt,dir,bind):
    if Check_if_Full() == 5540 and cnt > 150:
        time.sleep(10)
        pyautogui.press(bind)
        time.sleep(1)
        pyautogui.press('enter')
        time.sleep(1)
        pyautogui.press('enter')
        time.sleep(20)
        dir = "up"
        cnt = 0
        return dir, cnt
    return dir,cnt

def PickUp():
    pyautogui.press('x')
