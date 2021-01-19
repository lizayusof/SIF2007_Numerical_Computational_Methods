#insert your name here
#insert your new matrix number here


#importing the modules
import numpy as np
import matplotlib.pyplot as mpl

#This is general form, modify accordingly for a given problem
#function of ODEs
def f(x,y):
  return y*(np.sin(x))/x

#exact solution
def exact(x):
    return 1.0-np.exp(-x)


#initialised input (standard). You may add more initial data to suit your problem
x0 = 0.0
y0 = 2.0
n = 10
h = (1.0-0)/n


#Euler Method

#print header
print('x0','y0','yi','exact','error')
for i in range(0,n):
    yi = y0 + h*f(x0,y0) #euler's method
    error = np.abs(yi-exact(x0))
    print(x0,y0,yi,exact(x0),error)
    y0 = yi
    x0 = x0+h
    mpl.plot(x0,yi,'ok') #plot from Euler's method

#plot for analytical result
#modify the xnew accordingly
xnew = np.arange(0,1.5,0.1)
ynew = exact(xnew)
mpl.plot(xnew,ynew)

mpl.show()

