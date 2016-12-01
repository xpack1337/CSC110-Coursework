import scipy.integrate as integrate
import numpy
from scipy.optimize import fmin
import sympy.diff as derivative

def simpson(f, a, b, n):
    h=float((b-a)/n)
    k=0.0
    x=a + h
    for i in range(1,int(n/2 + 1)):
        k += 4*f(x)
        x += 2*h

    x = a + 2*h
    for i in range(1,int(n/2)):
        k += 2*f(x)
        x += 2*h
    return (h/3)*(f(a)+f(b)+k)

def trapezoidal(f, a, b, n):
    h = float((b - a) / n)
    summ = 0.0
    summ += f(a)/2.0
    for i in range(1, n):
        summ += f(a + i*h)
    summ += f(b)/2.0
    return summ * h

def errorbound (f, a, b, n):
    return fmin(derivative(derivative(f, x), x), 0)*((b-a)**3)/(12*n**2)

#creating integral
function =  lambda x: numpy.log(1/numpy.sin(x)**2)
myInt = integrate.quad(function,numpy.pi/3,numpy.pi/2)
#Output
print ("I = ",max(myInt))
print ("T_10 = ",trapezoidal(function,numpy.pi/3,numpy.pi/2,10))
print ("S_10 = ",simpson(function,numpy.pi/3,numpy.pi/2,10))
print (errorbound(function, numpy.pi/3,numpy.pi/2,10))
