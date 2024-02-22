
#ex1
import math
def radians(n):
    rad = n*(math.pi/180)
    print(rad)

n = int(input())
radians(n)


#Ex2

import math

def trapezoid(h, a, b):
    area = (a+b)*h/2
    print(area)

x = float(input())
y = float(input())
z = float(input())
trapezoid(x, y, z)


#Ex3
import math
def polig(n, m):
    if n == 4:
        area = ((m/2)*m*n)/2
        print(area)
    elif n > 4:
        a = 360/(2*n)
        if a == 30:
            a1 = (m/2)*3**0.5
            ar = (a1*m*n)/2
            print(ar)
        elif a == 60:
            a2 = (m/2)/3**0.5
            ar1 = (a2*m*n)/2
            print(ar1)
        if a == 45:
            a3 = m/2
            ar3 = (a3*m*n)/2
            print(ar3)
        else:
            a4 = (m/2)/math.tan((math.pi/180)*a)
            ar4 = (a4*m*n)/2
            print(ar4)


x = float(input())
y = float(input())
polig(x, y)


#ex4

def parall(a, h):
    area = a*h
    print(area)

x = float(input())
y = float(input())
parall(x, y)



