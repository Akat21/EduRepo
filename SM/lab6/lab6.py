import numpy as np
import matplotlib.pyplot as plt

img = plt.imread('./lab6/low_q.jpg', format='jpg')

x = np.array([len(img)])
x = np.concatenate([x,img.shape])
print(x)
shape = x[1:int(x[0]+1)]
data = img

def RLE_encoding(data):
    height, width, shape = data.shape
    data = data.flatten()

    result = []
    count = 1

    for i in range(len(data)):
        if i == len(data)-1 or data[i] != data[i+1]:
            result.append(count)
            result.append(data[i])
            count = 1
        else:
            count += 1
    return [result, height, width, shape]

def RLE_decoding(data):
    data, height, width, shape = data

    result = []
    i = 0
    while i < len(data):
        count = data[i]
        value = data[i+1]
        result.extend([value]*count)
        i += 2

    reshaped_data = np.array(result).reshape((height, width , shape))
    return reshaped_data

def ByteRun_encoding(data):
    height, width, shape = data.shape
    data = data.flatten()

    result = []
    count = 1
    curr_byte = data[0]

    for i in range(1, len(data)):
        if data[i] != curr_byte: # count == 127 or data[i] != curr_byte: jezeli bysmy chcieli robic limit 127 bitow
            if count == 1:
                result.append(curr_byte)
            else:
                result.append(-count + 1)
                result.append(curr_byte)
            count = 1
            curr_byte = data[i]
        else:
            count += 1

    if count == 1:
        result.append(curr_byte)
    else:
        result.append(-count + 1)
        result.append(curr_byte)

    return [result, height, width, shape]

def Byterun_decoding(data):
    data, height, width, shape = data

    result = []
    i = 0

    while i < len(data):
        if data[i] < 0:
            result.extend([data[i+1]] * (-data[i] + 1))
            i += 2
        else:
            result.extend([data[i]])
            i += 1

    reshaped_data = np.array(result).reshape((height, width, shape))
    return reshaped_data

print(data)
encoded_data = RLE_encoding(data)
decoded_data = RLE_decoding(encoded_data)
print(np.unique(decoded_data == data))

encoded_data = ByteRun_encoding(data)
print(encoded_data)
decoded_data = Byterun_decoding(encoded_data)
print(np.unique(data == decoded_data))
