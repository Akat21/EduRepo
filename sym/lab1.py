import numpy as np
from scipy import interpolate
import matplotlib.pyplot as plt

x=[-3,-2.5,-2,-1.5,-1,-0.5,0,0.5,1,1.5,2,2.5,3]
y=[-0.2,-0.1,0.6,0.9,0.4,-0.25,0,0.25,-0.4,-1,-0.6,0.2,0.2]

#zad1

#nearest#
xzad = 0.75
f = interpolate.interp1d(x,y,kind='nearest')
ynew = f(xzad)
err = abs(xzad - ynew)
plt.plot(x, y, "og-", xzad, ynew, "or")
plt.title("nearest" + err)
plt.show()
#linear#
f = interpolate.interp1d(x,y,kind='linear')
ynew = f(xzad)
plt.plot(x, y, "og-", xzad, ynew, "or")
plt.title("linear" + err)
plt.show()
#spline#
f = interpolate.interp1d(x,y,kind='quadratic')
ynew = f(xzad)
plt.plot(x, y, "og-", xzad, ynew, "or")
plt.title("quadratic" + err)
plt.show()
#cubic#
f = interpolate.interp1d(x,y,kind='cubic')
ynew1 = f(xzad)
plt.plot(x, y, "og-", xzad, ynew, "or")
plt.title("cubic" + err)
plt.show()

# #zad2

# #nearest
xx = np.linspace(-3,3,1000)
f = interpolate.interp1d(x, y, kind='nearest')
ynew = f(xx)
plt.plot(xx,ynew)
plt.title("nearest")
plt.show()

#linear
f = interpolate.interp1d(x, y, kind='linear')
ynew = f(xx)
plt.plot(xx,ynew)
plt.title("linear")
plt.show()

#spline#
f = interpolate.interp1d(x,y,kind='quadratic')
ynew = f(xx)
plt.plot(xx,ynew)
plt.title("quadratic")
plt.show()

#cubic#
f = interpolate.interp1d(x,y,kind='cubic')
ynew = f(xx)
plt.plot(xx,ynew)
plt.title("cubic")
plt.show()

#zad3
for i in range(len(x)):
    pp = np.polyfit(x,y,i)
    ya = np.polyval(pp,xx)
    plt.plot(x,y,'o')
    plt.plot(xx,ya,'-')
    plt.title(str(i))
    plt.show()
    msc = np.mean((y-np.polyval(pp,x))**2)
    print(msc)

pp = np.polyfit(x,y,10)
ynew = np.polyval(pp,0.75)
err = abs(ynew1 - ynew)
print(err)