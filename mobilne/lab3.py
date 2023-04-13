import numpy as np

#BiQuad
#802.11ac
print("BiQuad\n802.11ac")
f = 5.8 * 1000000000
c = 300000000
wavelength = c / f

L1 = wavelength/4
B = wavelength/2
H = wavelength
D = wavelength/8

L2 = L1*8 + D
max_length = 8 * L1 + D + 2*H + 2*B

print("L1: ", L1, "L2: ", L2, "B: ", B, "H: ", H, "D: ", D ,"Całkowita długość drutu: ", max_length)

#802.11g
print("BiQuad\n802.11g")
f = 2.4 * 1000000000
c = 300000000
wavelength = c / f

L1 = wavelength/4
B = wavelength/2
H = wavelength
D = wavelength/8

L2 = L1*8 + D
max_length = 8 * L1 + D + 2 * H + 2 * B

print("L1: ", L1, "L2: ", L2, "B: ", B, "H: ", H, "D: ", D, "Całkowita długość drutu: ", max_length)

#Yagi-Uda
#802.11g
print("Yagi-Uda\n802.11g")
f = 2.4 * 1000000000
c = 300000000
wavelength = c / f
radiators_n = 7
radiator_l = 0.47 * wavelength
reflektor_l = 0.49 * wavelength
direktor_l = 0.44 * wavelength
reflektor_radiator = 0.25 * wavelength
radiator_direktor = 0.20 * wavelength

max_length = reflektor_l + reflektor_radiator + radiators_n * (radiator_l + radiator_direktor) + radiator_direktor + direktor_l

print("Całkowita długość drutu: ", max_length)

#802.11ac
print("Yagi-Uda\n802.11ac")
f = 5.8 * 1000000000
c = 300000000
wavelength = c / f
radiators_n = 7
radiator_l = 0.47 * wavelength
reflektor_l = 0.49 * wavelength
direktor_l = 0.44 * wavelength
reflektor_radiator = 0.25 * wavelength
radiator_direktor = 0.20 * wavelength

max_length = reflektor_l + reflektor_radiator + radiators_n * (radiator_l + radiator_direktor) + radiator_direktor + direktor_l

print("Całkowita długość drutu: ", max_length)

#LOG-PER
#802.11g
print("LOG-PER\n802.11g")
f = 2.4 * 1000000000
c = 300000000
wavelength = c / f
T = 0.7
dipols = 8

I0 = wavelength/2
I1 = T*I0

l = [I0]
for i in range(1, dipols, 1):
    l.append(0)
    l[i] = l[i-1]*T

print("Długości poszczególnych dipoli(dla 8):", l, "Całkowita Długość: ", sum(l))
