import numpy as np
import matplotlib.pyplot as plt
import cv2

img1 = plt.imread("./lab1/B01.jpg")
img2 = cv2.imread("./lab1/B01.jpg")
img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2RGB)

print(img1.dtype)
print(img1.shape)
print(np.min(img1), np.max(img1))

##ZAD1
def imgToUint8(img):
    if np.issubdtype(img.dtype, np.uint8):
        return img
    else:
        return (img * 255).astype('uint8')

def imgToFloat(img):
    if np.issubdtype(img.dtype, np.float):
        return img
    else:
        return img/255.0
#######

##ZAD2
def convertToGrayY2(img):        
    R = img[:,:,0] * 0.2126
    G = img[:,:,1] * 0.7152
    B = img[:,:,2] * 0.0722
    Y2 = R + G + B
    return Y2

def convertToGrayY1(img):        
    R = img[:,:,0] * 0.299
    G = img[:,:,1] * 0.587
    B = img[:,:,2] * 0.114
    Y1 = R + G + B
    return Y1

def DrawOut(img): 
    #oryginalny
    plt.subplot(3,3,1)
    plt.imshow(img)

    #Y1
    plt.subplot(3,3,2)
    plt.imshow(convertToGrayY1(img), cmap=plt.cm.gray)

    #Y2
    plt.subplot(3,3,3)
    plt.imshow(convertToGrayY2(img), cmap=plt.cm.gray)

    #R
    R = img[:,:,0] * 0.299
    plt.subplot(3,3,4)
    plt.imshow(R, cmap=plt.cm.gray)

    #G
    G = img[:,:,1] * 0.587
    plt.subplot(3,3,5)
    plt.imshow(G, cmap=plt.cm.gray)

    #B
    B = img[:,:,2] * 0.114
    plt.subplot(3,3,6)
    plt.imshow(R, cmap=plt.cm.gray)

    #R0
    img_R0 = img.copy()
    for i in range(3):
        if i != 0:
            img_R0[:,:,i] = 0
    plt.subplot(3,3,7)
    plt.imshow(img_R0, cmap=plt.cm.gray)

    #G0
    img_G0 = img.copy()
    for i in range(3):
        if i != 1:
            img_G0[:,:,i] = 0
    plt.subplot(3,3,8)
    plt.imshow(img_G0, cmap=plt.cm.gray)

    #B0
    img_B0 = img.copy()
    for i in range(3):
        if i != 2:
            img_B0[:,:,i] = 0

    plt.subplot(3,3,9)
    plt.imshow(img_B0, cmap=plt.cm.gray)
parametr = "Normal"
DrawOut(img1)
plt.savefig("Colors-{}".format(parametr))
######

##ZAD3
parametr = "Normal"
img = plt.imread('B02.jpg')
fragment = img[500:700, 600:800].copy()
DrawOut(fragment)
plt.savefig("Tęcza-{}".format(parametr))
######