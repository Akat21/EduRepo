import numpy as np
import matplotlib.pyplot as plt
import scipy.fftpack
import sounddevice as sd
import soundfile as sf

data, fs = sf.read('sin_440Hz.wav', dtype='float32')

print(data.dtype)
print(data.shape)
print(fs)

# sd.play(data, fs)
# status = sd.wait()

##ZADANIE 1
def Zadanie1():
    if len(data) != 2:
        sf.write('sound_L.wav', data[:,0], fs)
        sf.write('sound_R.wav', data[:,1], fs)
        sf.write('sound_mix.wav', data[:,0]/2 + data[:,1]/2, fs)

        ###WYRYSYOWNE 2 KANAŁY DZWIEKOWE
        plt.subplot(2,1,1)
        plt.plot(np.arange(0,data.shape[0])/fs, data[:,0])

        plt.subplot(2,1,2)
        plt.plot(np.arange(0,data.shape[0])/fs, data[:,1])
        plt.show()

    #####WIDMO
    else:
        ####DOMYSLNY FSIZE(SIZE yf)
        plt.subplot(2,1,1)
        plt.plot(np.arange(0,data.shape[0])/fs, data)

        plt.subplot(2,1,2)
        yf = scipy.fftpack.fft(data)
        plt.plot(np.arange(0,fs,1.0*fs/(yf.size)), np.abs(yf))
        plt.show()

        #####FSIZE == 256
        fsize = 2**8

        plt.subplot(2,1,1)
        plt.plot(np.arange(0,data.shape[0])/fs, data)

        plt.subplot(2,1,2)
        yf = scipy.fftpack.fft(data,fsize)
        plt.plot(np.arange(0,fs,fs/fsize), np.abs(yf))
        plt.show()

        #####ODICIECIE POLOWY
        plt.subplot(2,1,1)
        plt.plot(np.arange(0,data.shape[0])/fs, data)

        plt.subplot(2,1,2)
        yf = scipy.fftpack.fft(data,fsize)
        plt.plot(np.arange(0,fs/2,fs/fsize), np.abs(yf[:fsize//2]))
        plt.show()

        #####PRZESKALOWANIE DO SKALI DECYBELOWEJ
        plt.subplot(2,1,1)
        plt.plot(np.arange(0,data.shape[0])/fs, data)

        plt.subplot(2,1,2)
        yf = scipy.fftpack.fft(data,fsize)
        plt.plot(np.arange(0,fs/2,fs/fsize), 20*np.log10(np.abs(yf[:fsize//2])))
        plt.show()


def plotAudio(Signal, fs, TimeMargin=[0,0.15]):
    fsize = 256
    plt.subplot(2,1,1)
    plt.plot(np.arange(0,Signal.shape[0])/fs, Signal)
    plt.xlim(TimeMargin)

    plt.subplot(2,1,2)
    yf = scipy.fftpack.fft(Signal,fsize)
    plt.plot(np.arange(0,fs/2,fs/fsize), 20*np.log10(np.abs(yf[:fsize//2])))
    plt.show()

plotAudio(data, fs)
