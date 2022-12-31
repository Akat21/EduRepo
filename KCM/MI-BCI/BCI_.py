import scipy.io
import scipy.signal
import numpy as np

Fs = 128
macierz_cech = []
pasma = np.array([[8,13], [13,30]])
cecha = 0
x_znormalizowane = []

mat = scipy.io.loadmat('dataset_BCIcomp1.mat')
X_train = np.array(mat['x_train'])
y_train = mat['y_train']
_b = []
_a = []
for i in range(2):
    a, b = scipy.signal.butter(4, pasma[i]/(Fs/2), 'bandpass')
    _b.append(b)
    _a.append(a)

for i in range(140):
    cecha = 0
    for k in range(2):
        for j in range(3):
            cecha += 1

            signal = X_train[:,j,i]
            signalFiltered = scipy.signal.lfilter(_a[k], _b[k], signal, axis = 0)
            macierz_cech.append(np.mean(signalFiltered**2))

print(macierz_cech)