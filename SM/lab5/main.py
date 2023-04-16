import numpy as np
import matplotlib.pyplot as plt
import sounddevice as sd
import scipy.fftpack
import soundfile as sf
from scipy.interpolate import interp1d

data, fs = sf.read('./lab5/sin_8000Hz.wav', dtype=np.int32)
print(fs)
# sin_data = np.sin(np.linspace(0, 10)) 
# plt.plot(sin_data)
# plt.show()

def plotAudio(Signal, fs, TimeMargin=[0,0.15]):
    fsize = 256
    plt.subplot(2,1,1)
    plt.plot(np.arange(0,Signal.shape[0])/fs, Signal)
    plt.xlim(TimeMargin)

    plt.subplot(2,1,2)
    yf = scipy.fftpack.fft(Signal,fsize)
    plt.plot(np.arange(0,fs/2,fs/fsize), 20*np.log10(np.abs(yf[:fsize//2])))
    plt.show()

def Kwant(data, bit):
    d = 2**bit - 1
    if np.issubdtype(data.dtype, np.floating):
        m = 0
        n = 1
    else:
        m = data.min()
        n = data.max()
    dataF = data.astype(float)
    dataF = (np.round((dataF - m) / (n - m) * d) / d * (n-m) + m).astype(int)
    return dataF.astype(data.dtype)

def Decymacja(data, n, fs):
    return data[::n], fs/n

def InterpLine(data, new_fs):
    x = np.linspace(0, int(np.round(len(data)/fs)), len(data))
    y = data
    T = len(data)/fs
    interp = interp1d(x, y)
    y_lin = interp(np.linspace(0, int(np.round(len(data)/fs)), int(np.ceil(new_fs*T)))).astype(y.dtype)
    return y_lin, new_fs

def InterpNonLine(data, new_fs):
    x = np.linspace(0, int(np.round(len(data)/fs)), len(data))
    y = data
    T = len(data)/fs
    interp = interp1d(x, y)
    y_lin = interp(np.linspace(0, int(np.round(len(data)/fs)), int(np.ceil(new_fs*T)))).astype(y.dtype)
    return y_lin, new_fs

data, fs = InterpLine(data, 41000)
# data, fs = InterpNonLine(data, 24000)
# data, fs = Decymacja(data, 6, fs)
# data = Kwant(data, 8)
# sd.play(data, fs)
# status = sd.wait()
plotAudio(data, fs, [0.005, 0.1])
# plt.plot(data)
# plt.show()

