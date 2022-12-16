import scipy.io
import scipy.signal
import numpy as np


Fs = 128

mat = scipy.io.loadmat('dataset_BCIcomp1.mat')
X_train = mat['x_train']
y_train = mat['y_train']

moc = []
for i in range(2):
    signal=X_train[:,i,i]
    [a,b] = scipy.signal.butter(6, np.array([13, 30])/(Fs/2),'bandpass')

    sygnalFiltered = scipy.signal.lfilter(a,b,signal)
    moc.append(np.mean(sygnalFiltered**2))

macierzCech = []
macierzCechFinal = []
for idx_proby in range(140):
    for idx_kanaly in range(3):
        for idx_pasma in range(2):
            signal = X_train[:,idx_kanaly,idx_proby]
            macierzCech.append(moc)
    macierzCechFinal.append(macierzCech)

