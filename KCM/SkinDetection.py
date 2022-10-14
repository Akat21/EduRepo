from colorsys import rgb_to_hsv
import matplotlib.pyplot as plt
import matplotlib.image as image
import matplotlib.colors as colors
import numpy as np
import cv2

def NormalizeData(data):
    return (data - np.min(data)) / (np.max(data) - np.min(data))

lower = np.array([0, 48, 80], dtype = "uint8")
upper = np.array([20, 255, 255], dtype = "uint8")

img = cv2.imread("hand.jpg")
img_hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
skinMask = cv2.inRange(img_hsv, lower, upper)
skin = cv2.bitwise_and(img, img, mask = skinMask)
skin[skin != 0] = 255
plt.imshow(skin)
plt.show() 
