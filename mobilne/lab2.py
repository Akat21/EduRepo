import numpy as np

f = 1000
d = 10

def swobodna(f, d):
    return -27.55 + 20 * np.log10(f) + 20 * np.log10(d)

def ITU_R(f, d, N, Lf):
    return 20 * np.log10(f) + N * np.log10(d) + Lf - 28

def OneSlope(d, L0, lmbda):
    return swobodna(f, d) + 10*lmbda*np.log(d)

def MotleyKeenan(f, d, nw, Lw, nf, Lf):
    return swobodna(f, d) + nw * Lw + nf * Lf

def MultiWall(d, L0, lmbda, kw, Lw, kf, Lf):
    return L0 + 10 * lmbda * np.log(d) + np.sum(kw*Lw) + np.sum(kf*Lf)

def EnBilans(Pn, Gn, Go, L, A):
    return Pn + Gn + Go - L - A


d = 80
f = 5220
nw = 2
ns = 4
print("Tłumienie w postaci swobodnej: ", swobodna(f, d))
print("ITU-R P.1238: ", ITU_R(f, d, 31, 1))
print("OneSlope: ", OneSlope(d, swobodna(f, d), 3))
print("Motley Keendan: ", MotleyKeenan(f, d, nw, 9, ns, 20))
print("Model Multi-Wall: ", MultiWall(d, swobodna(f,d ), 3, nw, 9, ns, 11))
print("Bilans Energetyczny: ", EnBilans(50, 50, 50, swobodna(f, d), 50))