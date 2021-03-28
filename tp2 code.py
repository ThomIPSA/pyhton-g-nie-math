import math


def PointFixe(g, x0, epsilon, Nitermax):
    xold = x0
    xnew = g(xold)
    n = 1
    while abs(xnew-xold) > epsilon and n < Nitermax :
        xold = xnew
        xnew = g(xold)
        n+=1
    return xnew, n

#exemple avec la fonction étudiée lors du TP1

def g0(x):
    return(1+math.sin(x))/2

print(PointFixe(g0, 0, 10**(-6), 5*10**(4)))



#Equations et leurs différentes formes étudiées pour le TP2 

#équation 1

def g1(x):
    return((9-3*x)**(1/4))
print(PointFixe(g1, 1, 10**(-10), 50000))


def g12(x):
    return (-(9-3*x)**(1/4))
print(PointFixe(g12, 1, 10**(-10), 50000))



#équation 2

def g21(x):
    return(3*math.cos(x)-2)
print(PointFixe(g21, 0, 10**(-6), 5*10**(4)))


def g22(x):
    return(math.acos((x+2)/3))
print(PointFixe(g22, 1, 10**(-6), 5*10**(4)))


def g23(x):
    return((-1)*math.acos((x+2)/3))
print(PointFixe(g23, 1, 10**(-6), 5*10**(4)))



#équation 3

def g3(x):
    return(math.log(7/x))
print(PointFixe(g3, 2, 10**(-10), 50000))



#équation 4

def g41(x):
    return(math.exp(x)-10)
print(PointFixe(g41, 2, 10**(-6), 5*10**(4)))

def g42(x):
    return(math.log(10+x))
print(PointFixe(g42, 2, 10**(-6), 5*10**(4)))



#équation 5

def g5(x):
    return(math.atan((x+5)/2))
print(PointFixe(g5, -5, 10**(-10), 50000))



#équation 6

def g61(x):
    return(math.log((x**2)+3))
print(PointFixe(g61, 2, 10**(-6), 5*10**(4)))



#équation 7

def g7(x):
    return((7-4*math.log(x))/3)
print(PointFixe(g7, 1, 10**(-10), 50000))



#équation 8

def g81(x):
    return((2*(x**2))-(4*x)+17)**(1/4)
print(PointFixe(g81, 2, 10**(-6), 5*10**(4)))


def g82(x):
    return (-1)*((2*(x**2))-(4*x)+17)**(1/4)
print(PointFixe(g82, (-2), 10**(-6), 5*10**(4)))



#équation 9

def g9(x):
    return(math.log(7+2*math.sin(x)))
print(PointFixe(g9, 2, 10**(-10), 50000))



#équation 10

def g10(x):
    return math.log(10)-math.log(math.log((x**2)+4))
print(PointFixe(g10, (3/2), 10**(-6), 5*10**(4)))


