import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def imgToFloat(img):
    if np.issubdtype(img.dtype, np.float32):
        return img
    else:
        return img/255.0

img = plt.imread('./lab4/low_q.jpg', format='jpg')

palette8 = np.array([
        [0.0, 0.0, 0.0,],
        [0.0, 0.0, 1.0,],
        [0.0, 1.0, 0.0,],
        [0.0, 1.0, 1.0,],
        [1.0, 0.0, 0.0,],
        [1.0, 0.0, 1.0,],
        [1.0, 1.0, 0.0,],
        [1.0, 1.0, 1.0,],
])

palette16 =  np.array([
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


palette255 = np.array(sns.color_palette("Spectral", 255))
# palette255 = np.round(np.array(palette255) * 255).astype(int)


##KWANTYZACJA##
def colorFit(pixel, pallet):
    if(type(pixel) != np.ndarray):
        pts = np.abs(pallet - pixel)
        return pallet[np.argmin(pts)]
    else:
        pts = np.abs(pallet - pixel)
        pts = np.linalg.norm(pts, axis=1)
        return pallet[np.argmin(pts)]

def kwant_colorFit(img, pallet):
    if(len(img.shape) < 3):
        height, width = img.shape
    else:
        height, width, dim = img.shape


    img = imgToFloat(img)
    out_img = img.copy()

    for i in range(height):
        for j in range(width):
            out_img[i, j] = colorFit(img[i, j], pallet)
    return out_img

###
def dithering_r(img):
    img = imgToFloat(img)
        
    height, width = img.shape
    r = np.random.rand(height, width)
    binary_img = (img >= r) * 1

    return binary_img
    
def dithering_o(img, pallet):
    if (len(img.shape) < 3):
        height, width = img.shape
    else:
        height, width, dim = img.shape

    out_img = img.copy()
    out_img = imgToFloat(out_img)
    
    n = 2
    M1 = np.array([[0, 2], [3, 1]])
    M2 = np.array([[0,8,2,10],[12,4,14,6],[3,11,1,9],[15,7,13,5]])

    Mpre = (M2 + 1) / (2*n)**2 - 0.5

    r = int(np.round(((pallet.max()*255 - pallet.min()*255) / (img.max() - img.min()))))

    img = imgToFloat(img)
    for i in range(height):
            for j in range(width):
                a = i % (2*n)
                b = j % (2*n)
                out_img[i, j] = colorFit(img[i, j] + r * Mpre[a, b], pallet)

    return out_img
    
def dithering_fs(img, pallet):
    if (len(img.shape) < 3):
        height, width = img.shape
    else:
        height, width, dim = img.shape

    out_img = img.copy()
    out_img = imgToFloat(out_img)
    

    for i in range(height):
        for j in range(width):
            oldpixel = out_img[i, j].copy()
            newpixel = colorFit(oldpixel, pallet)
            out_img[i, j] = newpixel
            quant_error = oldpixel - newpixel
            if(i == (height - 1) and j == (width - 1)):
                continue
            elif(i == (height - 1)):
                out_img[i - 1, j + 1] = out_img[i - 1, j + 1] + quant_error * 3 / 16
                out_img[i, j + 1] = out_img[i, j + 1] + quant_error * 5 / 16
            elif(j == (width - 1)):
                out_img[i + 1, j] = out_img[i + 1, j] + quant_error * 7 / 16
            else:
                out_img[i + 1, j] = out_img[i + 1, j] + quant_error * 7 / 16
                out_img[i - 1, j + 1] = out_img[i - 1, j + 1] + quant_error * 3 / 16
                out_img[i, j + 1] = out_img[i, j + 1] + quant_error * 5 / 16
                out_img[i + 1, j + 1] = out_img[i + 1, j + 1] + quant_error * 1 / 16
    return out_img

new_img = dithering_fs(img, palette8)
plt.imshow(new_img)
plt.show()