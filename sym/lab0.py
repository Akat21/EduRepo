import numpy as np
from matplotlib import cm
import matplotlib.pyplot as plt

x = np.linspace(0.1,4)

def f1(x):
    return np.sin(x) + np.cos(x)

def f2(x):
    return np.exp(x) + np.log(x)

def f3(x, y):
    return np.sin(x) + np.cos(x)

plt.plot(x, f1(x),'r')
plt.plot(x,f2(x))
plt.legend(['sin(x) + cos(x)', 'e^x + log(x)'])
plt.show()

x = np.linspace(-2*np.pi, 2*np.pi)
y = np.linspace(-2*np.pi, 2*np.pi)

#aby wyznaczyć Z musimy użyć meshgrida na naszych wartościach x,y 
xx, yy = np.meshgrid(x,y)
zz = f3(xx,yy)

#rysowanie 3D plota
fig, ax = plt.subplots(subplot_kw={"projection" : "3d"})

ax.plot_surface(xx, yy, zz, cmap='viridis')
#####

#uniform wypisuje random floaty z przedzialu o wielkosci size
ran_x = np.random.uniform(2,5, size = 7)
ran_y = np.random.uniform(3,7, size = 7)
ran_points = np.column_stack((ran_x, ran_y))

def draw_points(x, y):
    #scatter rysuje punkty
    for i in range(len(x)):
        ax.scatter(x[i], y[i], marker='s', c='red', s=15)
    for i in range(len(x) - 1):
        ax.plot([x[i], x[i+1]], [y[i], y[i+1]], c='black', linestyle='--', linewidth=3)

draw_points(ran_x, ran_y)
plt.show()