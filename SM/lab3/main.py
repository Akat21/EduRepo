import numpy as np
import matplotlib.pyplot as plt

img = plt.imread("./lab3/B01.jpg")
scale = 1.5

plt.imshow(img)
plt.title('Orginalny obraz')
plt.savefig('./lab3/B01_original.jpg', format = 'jpg')
plt.show()

#Nearest Neighbors
def NN():
    if(len(img.shape) < 3):
        pass
    else:
        height, width, dim = img.shape
        new_width, new_height = int(width * scale), int(height * scale)

        scaled_img = np.zeros((new_height, new_width, dim), dtype = np.uint8)

        for i in range(new_height):
            for j in range(new_width):
                x = int(min(j / scale, width - 1))
                y = int(min(i / scale, height - 1))
                scaled_img[i, j] = img[y, x]

        plt.imshow(scaled_img)
        plt.title('Obraz powiększony o ' + str((scale - 1) * 100) + '%' + ' Nearest Neighbors')
        plt.savefig('./lab3/B01_scaled.jpg', format = 'jpg')

#Interpolation
def interpol():
    if(len(img.shape) < 3):
        pass
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
        
        plt.imshow(scaled_img)
        plt.title('Obraz powiększony o ' + str((scale - 1) * 100) + '%' + ' Bilinear Interpolation')
        plt.show()

scale = 0.5

#Mean Downscale
def DownScale_mean():
    height, width, dim = img.shape
    new_width, new_height = int(width * scale), int(height * scale)

    scaled_img = np.zeros((new_height, new_width, dim), dtype=np.uint8)

    for i in range(height):
        for j in range(width):

            neighborhood = img[max(0, i - 2):min(height, i + 3), max(0, j - 2):min(width, j + 3)]

            pixel_value = np.mean(neighborhood, axis=(0, 1))
            scaled_img[int(i * scale), int(j * scale)] = np.round(pixel_value).astype(np.uint8)
            
    plt.imshow(scaled_img)
    plt.show()

def DownScale_mediana():
    height, width, dim = img.shape
    new_width, new_height = int(width * scale), int(height * scale)

    scaled_img = np.zeros((new_height, new_width, dim), dtype=np.uint8)

    for i in range(height):
        for j in range(width):

            neighborhood = img[max(0, i - 2):min(height, i + 3), max(0, j - 2):min(width, j + 3)]

            pixel_value = np.median(neighborhood, axis=(0, 1))
            scaled_img[int(i * scale), int(j * scale)] = np.round(pixel_value).astype(np.uint8)
            
    plt.imshow(scaled_img)
    plt.show()

def DownScale_wage_mean():
    height, width, dim = img.shape
    new_width, new_height = int(width * scale), int(height * scale)

    scaled_img = np.zeros((new_height, new_width, dim), dtype=np.uint8)

    for i in range(height):
        for j in range(width):

            neighborhood = img[max(0, i - 2):min(height, i + 3), max(0, j - 2):min(width, j + 3)]

            pixel_value = np.average(neighborhood, axis=(0, 1))
            scaled_img[int(i * scale), int(j * scale)] = np.round(pixel_value).astype(np.uint8)
            
    plt.imshow(scaled_img)
    plt.show()

DownScale_wage_mean()