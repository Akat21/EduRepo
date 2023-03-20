import numpy as np
import matplotlib.pyplot as plt
import cv2

img = plt.imread("./lab3/high_q.jpg")
scale = 1.5
print(img.shape)
plt.imshow(img)
plt.title('Orginalny obraz')
plt.show()

plt.imshow(img)
plt.title('Wycinek Oryginalny')
plt.xlim([400, 550])
plt.ylim([250, 100])
plt.show()

edge = cv2.Canny(img, 50, 150)
plt.title("Wycinek Oryginalny Krawedzie")
plt.xlim([400, 550])
plt.ylim([250, 100])
plt.imshow(edge)
plt.show()

#Nearest Neighbors
def NN():
    if(len(img.shape) < 3):
        return 0
    else:
        height, width, dim = img.shape
        new_width, new_height = int(width * scale), int(height * scale)

        scaled_img = np.zeros((new_height, new_width, dim), dtype = np.uint8)

        for i in range(new_height):
            for j in range(new_width):
                x = int(min(j / scale, width - 1))
                y = int(min(i / scale, height - 1))
                scaled_img[i, j] = img[y, x]

        return scaled_img

#Interpolation
def interpol():
    if(len(img.shape) < 3):
        return 0
    else:
        height, width, dim = img.shape
        new_width, new_height = int(width * scale), int(height * scale)

        scaled_img = np.zeros((new_height, new_width, dim), dtype=np.uint8)

        for i in range(new_height):
            for j in range(new_width):
                x_in = j / scale
                y_in = i / scale

                x_low = np.floor(x_in).astype(int)
                y_low = np.floor(y_in).astype(int)

                x_weight = x_in - x_low
                y_weight = y_in - y_low

                x_index_1 = max(x_low - 1, 0)
                y_index_1 = max(y_low - 1, 0)
                x_index_2 = min(x_low + 1, width - 1)
                y_index_2 = min(y_low + 1, height - 1)

                p11 = img[y_index_1, x_index_1]
                p12 = img[y_index_2, x_index_1]
                p21 = img[y_index_1, x_index_2]
                p22 = img[y_index_2, x_index_2]

                pixel_value = (
                    (p11 * (1 - x_weight) * (1-y_weight)) + (p21 * x_weight * (1 - y_weight))
                    + (p12 * (1 - x_weight) * y_weight) + (p22 * x_weight * y_weight)
                )

                scaled_img[i, j] = np.round(pixel_value).astype(np.uint8)
        
        return scaled_img

scale = 0.7

#Mean Downscale
def DownScale_mean():
    if(len(img.shape) < 3):
        return 0
    else:
        height, width, dim = img.shape
        new_width, new_height = int(width * scale), int(height * scale)

        scaled_img = np.zeros((new_height, new_width, dim), dtype=np.uint8)

        for i in range(height):
            for j in range(width):

                neighborhood = img[max(0, i - 2):min(height, i + 3), max(0, j - 2):min(width, j + 3)]

                pixel_value = np.mean(neighborhood, axis=(0, 1))
                scaled_img[int(i * scale) - 1, int(j * scale) - 1] = np.round(pixel_value).astype(np.uint8)

        return scaled_img        

def DownScale_mediana():
    if(len(img.shape) < 3):
        return 0
    else:
        height, width, dim = img.shape
        new_width, new_height = int(width * scale), int(height * scale)

        scaled_img = np.zeros((new_height, new_width, dim), dtype=np.uint8)

        for i in range(height):
            for j in range(width):

                neighborhood = img[max(0, i - 2):min(height, i + 3), max(0, j - 2):min(width, j + 3)]

                pixel_value = np.median(neighborhood, axis=(0, 1))
                scaled_img[int(i * scale) - 1, int(j * scale) - 1] = np.round(pixel_value).astype(np.uint8)
                
        return scaled_img

def DownScale_wage_mean():
    if(len(img.shape) < 3):
        return 0
    else:
        height, width, dim = img.shape
        new_width, new_height = int(width * scale), int(height * scale)

        scaled_img = np.zeros((new_height, new_width, dim), dtype=np.uint8)
        print(new_height, new_width)
        for i in range(height):
            for j in range(width):

                neighborhood = img[max(0, i - 2):min(height, i + 3), max(0, j - 2):min(width, j + 3)]

                pixel_value = np.average(neighborhood, axis=(0, 1))
                scaled_img[int(i * scale) - 1, int(j * scale) - 1] = np.round(pixel_value).astype(np.uint8)

        return scaled_img

img = DownScale_wage_mean()
edge = cv2.Canny(img, 50, 150)
plt.title("Wycinek Przeskalowany Krawedzie")
plt.xlim(np.array([400, 550]) * 0.7)
plt.ylim(np.array([250, 100]) * 0.7)
plt.imshow(edge)
plt.show()
plt.imshow(img)
plt.title("Wycinek Przeskalowany")
plt.xlim(np.array([400, 550]) * 0.7)
plt.ylim(np.array([250, 100]) * 0.7)
plt.show()