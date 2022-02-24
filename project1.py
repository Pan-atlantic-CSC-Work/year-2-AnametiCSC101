#qudratic equation

import bisect
from cmath import sqrt


def quadratic(a,b,c):
    x1 =(((-1)*(b)) + sqrt(b**2-4*a*c))/(2*a)
    x2 = (((-1)*(b)) - sqrt(b**2-4*a*c))/(2*a)
    print(x1,x2)

quadratic(4,3,5);