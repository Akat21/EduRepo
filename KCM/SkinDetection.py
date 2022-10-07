import matplotlib.pyplot as plt
import matplotlib.image as image
import numpy as np

def rgb2hsv(image):
    return image.convert("HSV")

def NormalizeData(data):
    return (data - np.min(data)) / (np.max(data) - np.min(data))

img = image.imread("hand.jpg")
plt.imshow(img)
print(NormalizeData(img)[:,:,0])
plt.show()