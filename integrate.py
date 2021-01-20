#simpson

import numpy as np
from scipy.integrate import simps  


def f(x):
  return x*(1-x**2)

#exact = (1/3)*np.log(2)+(1/9)*np.sqrt(3)*np.pi

a = 0.0
b = 1.0
h = 0.25

#integration from the formula
s1 =((b-a)/6)*(f(a)+4*f((a+b)/2.0)+f(b))
s2 = h/(3.0)*(f(a)+4*f((a+b)/2.0)+f(b))


#integation using Simpson's method from Scipy module
xf = np.linspace(0,1.0, 4)
y = f(xf)
simpson = simps(y,xf)

#integration using trapeziod method from Scipy module
#xf = np.linspace(0,1.0, 4)
#y = f(xf)
#trap = trapezoid(y,xf)

print(s1,s2,simpson,trap)


#err1 = np.abs(s1-exact)
#err2 = np.abs(s2-exact)

#print(s1,s2,exact,err1,err2)
