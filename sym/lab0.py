import numpy as np
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

xx, yy = np.meshgrid(x,y)
zz = np.sqrt(xx**2 + yy**2)

fig = plt.figure()
ax = plt.axes(projection='3d')
ax.contour3D(xx,yy,zz,100,cmap='binary')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')

ran_x = np.random.uniform(2,5, size = 7)
ran_y = np.random.uniform(3,7, size = 7)
ran_points = np.column_stack((ran_x, ran_y))

def draw_points(x, y):
    for i in range(len(x)):
        ax.scatter(x[i], y[i], marker='s', c='red', s=15)

draw_points(ran_x, ran_y)
plt.show()