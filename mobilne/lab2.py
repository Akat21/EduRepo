import numpy as np

f = 1000
d = 10

def swobodna(f, d):
    return -27.55 + 20 * np.log10(f) + 20 * np.log10(d)

def ITU_R(f, d, N, Lf):
    return 20 * np.log(f) + N * np.log(d) + Lf - 28

def OneSlope(d, L0, lmbda):
    return L0 + 10*lmbda*np.log(d)

def MotleyKeenan(f, d, nw, Lw, nf, Lf):
    return swobodna(f, d) + nw * Lw + nf * Lf

def MultiWall(d, L0, lmbda, kw, Lw, kf, Lf):
    return L0 + 10 * lmbda * np.log(d) + np.sum(kw*Lw) + np.sum(kf*Lf)

def EnBilans(Pn, Gn, Go, L, A):
    return Pn + Gn + Go - L - A

#2m - -34db
print("Tłumienie w postaci swobodnej: ", swobodna(5220, 2))
print("ITU-R P.1238: ", ITU_R(5220, 2, 31, 1))
print("OneSlope: ", OneSlope(2, 25, 4.5))
print("Motley Keendan: ", MotleyKeenan(5220, 2, 0, 0, 0, 0))
print("Model Multi-Wall: ", MultiWall(2, 25, 4.5, 0, 0, 0, 0))
print("Bilans Energetyczny: ", EnBilans(50, 50, 50, swobodna(5220, 2), 50))