from sys import argv
import pandas as pd
import matplotlib.pyplot as plt
from scipy.signal import find_peaks
import numpy as np


def peaks(data):
    peak_idx , peak_val = find_peaks(data.to_numpy().flatten(), height = 0)
    return peak_idx, peak_val['peak_heights']

def read_EKG(file, fs = 360):
    A = pd.read_csv(file)
    One_sec = A[0:fs]
    Two_sec = A[0:fs*2]
    peak_idx , peak_val = find_peaks(Two_sec.to_numpy().flatten(), height = 0)
    cycle = A[peak_idx[0]:peak_idx[1]]
    HR = fs/(np.abs(peak_idx[1]-peak_idx[0]))*60
    print(HR)

    HR = []
    peak_idx, peak_val = peaks(A)
    for idx, el in enumerate(peak_idx):
        if idx == 0:
            continue
        else:
            if(el - peak_idx[idx-1] > 135):
                HR.append(fs/(np.abs(el-peak_idx[idx-1]))*60)

    print("\n", np.mean(HR))


    plt.plot(peak_idx, peak_val, "ro")
    plt.plot(A)
    plt.savefig("piki_100_V5.jpg", format = "jpg")
    plt.show()

read_EKG("ekg_sygnały/100_V5.dat")