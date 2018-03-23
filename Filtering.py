from UtilsTest import *
from PrintingMod import *

def filtering_real(l):
    new = []
    for i in range(len(l)):
        a,b = real_imaginary(l[i])
        if b == 0:
           new.append(l[i])
    return new

def filtering_modulos(l, char, no):
    new = []
    n = verifying_pos(no)
    if n == -1:
        return l
    lis = modulos(l)
    if char == "<":
        for i in range(len(lis)):
            if lis[i] < n:
                new.append(l[i])
    if char == "=":
        for i in range(len(lis)):
            if lis[i] == n:
                new.append(l[i])
    if char == ">":
        for i in range(len(lis)):
            if lis[i] > n:
                new.append(l[i])
    return new