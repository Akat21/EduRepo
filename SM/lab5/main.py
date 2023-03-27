import numpy as np
import matplotlib.pyplot as plt
import sounddevice as sd
import soundfile as sf

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



sin_data = Kwant(sin_data, 4)
plt.plot(sin_data)
plt.show()

