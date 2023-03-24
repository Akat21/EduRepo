import numpy as np

f = 1000
d = 10

def swobodna(f, d):
    return -27.55 + 20 * np.log10(f) + 20 * np.log10(d)

def ITU_R(f, d, N, Lf):
    return 20 * np.log10(f) + N * np.log10(d) + Lf - 28

def OneSlope(d, L0, lmbda):
    return swobodna(f, d) + 10*lmbda*np.log10(d)

def MotleyKeenan(f, d, nw, Lw, nf, Lf):
    return swobodna(f, d) + nw * Lw + nf * Lf

def MultiWall(d, L0, lmbda, kw, Lw, kf, Lf):
    return L0 + 10 * lmbda * np.log10(d) + np.sum(kw*Lw) + np.sum(kf*Lf)

def EnBilans(Pn, Gn, Go, L, A):
    return Pn + Gn + Go - L - A


d = 80
f = 5220
nw = 2
ns = 4
print("Tłumienie w postaci swobodnej: ", EnBilans(20, 20, 20, swobodna(f, d), 20))
print("ITU-R P.1238: ", EnBilans(20, 20, 20, ITU_R(f, d, 31, 1), 20))
print("OneSlope: ", EnBilans(20, 20, 20, OneSlope(d, swobodna(f, d), 2), 20))
print("Motley Keendan: ", EnBilans(20, 20, 20, MotleyKeenan(f, d, nw, 9, ns, 20), 20))
print("Model Multi-Wall: ", EnBilans(20, 20, 20, MultiWall(d, swobodna(f, d), 2, nw, 9, ns, 11), 20))