import numpy as np
import matplotlib.pyplot as plt

#Zad1
Gt, Gr = 1.6, 1.6
f1 = 900000000
f2 = 2400000000
c = 300000000

d = 1
lambdaa = 0.3
prpt = Gt * Gr * (lambdaa/(4*np.pi*d)) ** 2
prptdb = 10*np.log10(prpt)
print(prptdb)

#a
d = np.linspace(1, 100, 500)
PrPt1 = Gt * Gr*((c/f1)/(4*np.pi*d))**2
PrPtdb1 = 10*np.log10(PrPt1)

PrPt2 = Gt * Gr*((c/f2)/(4*np.pi*d))**2
PrPtdb2 = 10*np.log10(PrPt2)

plt.plot(d, PrPtdb1)
plt.plot(d, PrPtdb2)
plt.title('1-100m')
plt.xlabel('s(m)')
plt.ylabel('I(dB)')
plt.show()

#b
d = np.linspace(1, 10000, 5000) 
PrPt1 = Gt * Gr*((c/f1)/(4*np.pi*d))**2
PrPtdb1 = 10*np.log10(PrPt1)

PrPt2 = Gt * Gr*((c/f2)/(4*np.pi*d))**2
PrPtdb2 = 10*np.log10(PrPt2)

plt.plot(d, PrPtdb1)
plt.plot(d, PrPtdb2)
plt.title('1-10km')
plt.xlabel('s(m)')
plt.ylabel('I(dB)')
plt.show()

#Zad2
t = d/c
plt.plot(d, t)
plt.title('1-10km Opóznienie')
plt.xlabel('s(m)')
plt.ylabel('t(s)')
plt.show()