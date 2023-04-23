import numpy as np
import matplotlib.pyplot as plt
import soundfile as sf
import sounddevice as sd

sin_data, fs = sf.read('./lab7/sing_high2.wav', dtype=np.float32)
sd.play(sin_data, fs)
status = sd.wait()
# x=np.linspace(-1,1,1000)
# sin_data = 0.9 * np.sin(np.pi*x*4)
plt.plot(sin_data)
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
    dataF = (np.round((dataF - m) / (n - m) * d) / d * (n-m) + m)
    return dataF.astype(data.dtype)

def ALawEncoding(data, bit):
    A = 87.6
    
    Fx = data.copy()
    idx = Fx < (1/A) 
    idx2 = np.logical_and((1/A) <= np.abs(Fx), np.abs(Fx) <= 1)
    Fx[idx] = np.sign(data[idx]) * (A*np.abs(data[idx]))/(1 + np.log(A))
    Fx[idx2] = np.sign(data[idx2]) * (1 + np.log(A*np.abs(data[idx2])))/(1+np.log(A))
    Fx = Kwant(Fx, bit)
    return Fx

def ALawDecoding(data):
    A = 87.6
    Fy = data.copy()
    idx = np.abs(Fy) < (1/(1+np.log(A)))
    idx2 = np.logical_and( (1/(1+np.log(A))) <= np.abs(data), np.abs(data) <= 1 )
    Fy[idx] = np.sign(data[idx]) * (np.abs(data[idx])*(1+np.log(A)))/A
    Fy[idx2] = np.sign(data[idx2]) * (np.exp(np.abs(data[idx2])*(1+np.log(A)-1)))/A
    return Fy

def MuLawEncoding(data, bit):
    mu = 255
    Fx = data.copy()
    idx = np.logical_and(-1 <= data, data <= 1)
    Fx[idx] = np.sign(data[idx]) * ((np.log(1 + mu * np.abs(data[idx])))/np.log(1+mu))
    Fx = Kwant(Fx, bit)
    return Fx

def MuLawDecoding(data):
    mu = 255
    Fy = data.copy()
    idx = np.logical_and(-1 <= data, data <= 1)
    Fy[idx] = np.sign(data[idx]) * (1 / mu) * ( (1 + mu)**np.abs(data[idx]) - 1)
    return Fy


def DPCMEncoding(x, bit):
    y = np.zeros(x.shape)
    e = 0
    for i in range(0, x.shape[0]):
        y[i] = Kwant(x[i] - e, bit)
        e += y[i]
    return y

def DPCMDecoding(y):
    x = np.zeros(y.shape)
    e = 0
    for i in range(0,x.shape[0]):
        x[i] = y[i] + e
        e = x[i]
    return x

sin_data = DPCMEncoding(sin_data, 8)
sin_data = DPCMDecoding(sin_data)
plt.plot(sin_data)
plt.show()
sd.play(sin_data, fs)
status = sd.wait()