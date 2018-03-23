from UtilsTest import *
from math import *

def sum_pos(a, b, l):
    s = 0
    for i in range(a, b + 1):
        r, i = real_imaginary(l[i])
        z = complex(r, i)
        s = s + z

    return s

def product_pos(a, b, l):
    p = 1
    for i in range(a, b + 1):
        r, i = real_imaginary(l[i])
        z = complex(r, i)
        p = p * z

    return p