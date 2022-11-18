import matplotlib.pyplot as plt
import matplotlib.image as image
import numpy as np
import cv2

lower = np.array([0*255, 0.2*255, 0.4*255], dtype = "float")
upper = np.array([0.1*255, 0.6*255, 1*255], dtype = "float")

img0 = plt.imread("hand.jpg")
img = cv2.imread("hand.jpg")
img_hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
skinMask = cv2.inRange(img_hsv, lower, upper)

skin = cv2.bitwise_and(img, img, mask = skinMask)
skin[skin != 0] = 255

f, axarr = plt.subplots(1,2)
axarr[0].imshow(img0)
axarr[1].imshow(skin)
plt.show() 
