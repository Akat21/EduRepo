import numpy as np
import matplotlib.pyplot as plt

img = plt.imread("./lab3/B01.jpg")
scale = 1.5

plt.imshow(img)
plt.title('Orginalny obraz')
plt.savefig('./lab3/B01_original.jpg', format = 'jpg')

#Nearest Neighbors
if(len(img.shape) < 3):
    pass
else:
    height, width, dim = img.shape
    new_width, new_height = int(width * scale), int(height * scale)

    scaled_img = np.zeros((new_height, new_width, 3), dtype = np.uint8)
    for i in range(new_height):
        for j in range(new_width):
            x = int(min(j / scale, width - 1))
            y = int(min(i / scale, height - 1))
            scaled_img[i, j] = img[y, x]

    plt.imshow(scaled_img)
    plt.title('Obraz powiększony o ' + str((scale - 1) * 100) + '%' + ' Nearest Neighbors')
    plt.savefig('./lab3/B01_scaled.jpg', format = 'jpg')

#Interpolation
