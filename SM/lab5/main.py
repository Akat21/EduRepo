import numpy as np
import matplotlib.pyplot as plt
import sounddevice as sd
import soundfile as sf
from scipy.interpolate import interp1d

data, fs = sf.read('./lab5/sin_60Hz.wav', dtype='int32')

sin_data = np.sin(np.linspace(0, 10)) 
plt.plot(sin_data)
plt.show()

def Kwant(data, bit):
    d = bit
    if np.issubdtype(data.dtype, np.floating):
        m = 0
        n = 1
    else:
        m = data.min()
        n = data.max()
    dataF = data.astype(float)
    dataF = (np.round((data - m) / (n - m) * d) / d * (n-m) + m).astype(int)
    return dataF.astype(data.dtype)

def Decymacja(data, n):
    return data[::n], fs/n

def InterpLine(data, new_fs):
    x = np.linspace(0, len(data), len(data))
    y = data
    interp = interp1d(x, y)
    y_lin = interp(np.linspace(0, len(data), new_fs))
    return y_lin

def InterpNonLine(data, new_fs):
    x = np.linspace(0, len(data), len(data))
    y = data
    interp = interp1d(x, y, kind='cubic')
    y_lin = interp(np.linspace(0, len(data), new_fs))
    return y_lin

# data = InterpLine(data, 2400)
# data = InterpNonLine(data, 2400)
# data, fs = Decymacja(data, 10)
# data = Kwant(data, 32)
plt.plot(data)
plt.show()

