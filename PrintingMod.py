from UtilsTest import *

def printing_real(lsplit, l):
    if verifying_pos(lsplit[2]) != -1 and int(lsplit[2]) < len(l):
        a = int(lsplit[2])
    else:
        print("Invalid position")
        return
    if verifying_pos(lsplit[4]) != -1 and int(lsplit[4]) < len(l):
        b = int(lsplit[4])
    else:
        print("Invalid position")
        return
    if a > b:
        print("Invalid position")
        return
    ok = 0
    for i in range(a, b + 1):
        new = l[i]
        poz = new.find("i")
        if poz == -1:
            ok = 1
            print(new)
    if ok == 0:
        print("NONE")

def modulos(new):
    l = []
    for i in range(len(new)):
        a, b = real_imaginary(new[i])
        x = calculate_modulo(a, b)
        l.append(round(x, 2))

    return l

def printing_mod(l, lis, char, no):
    if char == "<":
        for i in range(len(lis)):
            if lis[i] < int(no):
                print(l[i])
    elif char == ">":
        for i in range(len(lis)):
            if lis[i] > int(no):
                print(l[i])
    else:
        for i in range(len(lis)):
            if lis[i] == int(no):
                print(l[i])