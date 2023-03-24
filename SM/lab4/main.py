import numpy as np
import matplotlib.pyplot as plt

def imgToFloat(img):
    if np.issubdtype(img.dtype, np.float32):
        return img
    else:
        return img/255.0
    
img = plt.imread('./lab4/high_q.jpg', format='jpg')
img = imgToFloat(img)

pallet8 = np.array([
        [0.0, 0.0, 0.0,],
        [0.0, 0.0, 1.0,],
        [0.0, 1.0, 0.0,],
        [0.0, 1.0, 1.0,],
        [1.0, 0.0, 0.0,],
        [1.0, 0.0, 1.0,],
        [1.0, 1.0, 0.0,],
        [1.0, 1.0, 1.0,],
])

pallet16 =  np.array([
        [0.0, 0.0, 0.0,], 
        [0.0, 1.0, 1.0,],
        [0.0, 0.0, 1.0,],
        [1.0, 0.0, 1.0,],
        [0.0, 0.5, 0.0,], 
        [0.5, 0.5, 0.5,],
        [0.0, 1.0, 0.0,],
        [0.5, 0.0, 0.0,],
        [0.0, 0.0, 0.5,],
        [0.5, 0.5, 0.0,],
        [0.5, 0.0, 0.5,],
        [1.0, 0.0, 0.0,],
        [0.75, 0.75, 0.75,],
        [0.0, 0.5, 0.5,],
        [1.0, 1.0, 1.0,], 
        [1.0, 1.0, 0.0,]
])

##KWANTYZACJA##
def colorFit(pixel, pallet):
    if(len(img.shape) < 3):
        pts = np.abs(pallet - pixel)
        return pallet[np.argmin(pts)]
    else:
        pts = np.abs(pallet - pixel)
        pts = np.linalg.norm(pts, axis=1)
        return pallet[np.argmin(pts)]

def kwant_colorFit(img, pallet):
    if(len(img.shape) < 3):
        out_img = img.copy()
        height, width = img.shape

        for i in range(height):
            for j in range(width):
                out_img[i, j] = colorFit(img[i, j], pallet)
    else:
        out_img = img.copy()
        height, width, dim = img.shape

        for i in range(height):
            for j in range(width):
                out_img[i, j] = colorFit(img[i, j], pallet)
    return out_img

###
# q_img = kwant_colorFit(img, pallet8)
def dithering(img):
    if(len(img.shape) < 3):
        height, width = img.shape
        r = np.random.rand(height, width)
        binary_img = (img >= r) * 1
        return binary_img
    else:
        gray_img = np.dot(img[...,:3], [0.2989, 0.5870, 0.1140])
        
        height, width = gray_img.shape
        r = np.random.rand(height, width)
        binary_img = (gray_img >= r) * 1
        return binary_img

new_img = dithering(img)
print(new_img)
plt.imshow(new_img)
plt.show()