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
    img = imgToFloat(img)
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
def dithering(img):
    img = imgToFloat(img)
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

        rgb_img = np.zeros((*binary_img.shape, 3), dtype=np.uint8)
        rgb_img[..., 0] = binary_img
        rgb_img[..., 1] = binary_img
        rgb_img[..., 2] = binary_img

        return rgb_img * 255
    
def dithering_o(img, pallet):
    if (len(img.shape) < 3):
        pass
    else:
        out_img = img.copy()
        out_img = imgToFloat(out_img)
        
        n = 2
        M1 = np.array([[0, 2], [3, 1]])
        M2 = np.array([[0,8,2,10],[12,4,14,6],[3,11,1,9],[15,7,13,5]])

        Mpre = (M2 + 1) / (2*n)**2 - 0.5

        height, width, dim = img.shape

        r = int(np.round(((pallet.max()*255 - pallet.min()*255) / (img.max() - img.min()))))

        img = imgToFloat(img)
        for i in range(height):
                for j in range(width):
                    a = i % (2*n)
                    b = j % (2*n)
                    out_img[i, j] = colorFit(img[i, j] + r * Mpre[a, b], pallet)

        return out_img

new_img = dithering(img)
plt.imshow(new_img)
plt.show()