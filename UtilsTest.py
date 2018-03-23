from math import *

def verifying_pos(n):
    try:
        poz = int(n)
    except ValueError as ve:
        print("Invalid position, ", ve)
        return -1
    return poz

def verifying(number):
    new = number
    poz = new.find("+")
    if poz == -1:
        poz = new.find("-", 1)
    if poz == -1:
        if new[len(new) - 1] != "i":
            try:
                a = int(new)                            #verifying if its an integer with imaginary part = 0
            except ValueError as ve:
                print("Invalid number1, ", ve)
                return -1
            return 1
        if new[len(new) - 1] == "i" and new[0] != "-":
            try:
                a = int(new[:-1])                            #verifying if its an integer with imaginary part = 0
            except ValueError as ve:
                print("Invalid number1, ", ve)
                return -1
            return 1
    if len(new) == 2 and new[1] == "i":
        return 1
    if new[poz + 1] == "i":
        try:
            a = new[poz + 2]
        except IndexError as ie:                        #verif. if after the symbol is "i"
            return 1
    try:
        a = int(new[:poz])
        b = int(new[poz + 1:-1])                        #verif. if before and after the symbol is an integer
    except ValueError as ve:
        print("Invalid number, ", ve)
        return -1
    return 1

def calculate_modulo(a, b):
    a = a**2
    b = b**2

    return sqrt(a + b)

def real_imaginary(n):
    new = n
    if len(new) == 1 and new[0] == "i":
        return 0, 1
    poz = new.find("+")
    if poz == -1:
        poz = new.find("-", 1)
    if poz == -1:
        if new[len(new) - 1] != "i":
            try:
                a = int(new)  # verifying if its an integer with imaginary part = 0
            except ValueError as ve:
                return -1, -1
            return a,0
        if new[len(new) - 1] == "i" and new[0] != '-':
            try:
                a = int(new[:-1])
            except ValueError as ve:
                return -1, -1
            return 0, a
        elif new[len(new) - 1] == "i" and new[0] == '-' and len(new) == 2:
            return 0, -1
        if new[len(new) - 1] == 'i' and new[0] == '-' and len(new) != 2:
            return 0, -int(new[1:-1])

    if len(new) == 2 and new[1] == "i" and new[0] != '-':
        return 0, int(new[0])
    if len(new) == 1 and new[0] == "i":
        return 0, 1
    if new[poz + 1] == "i":
        try:
            a = new[poz + 2]
        except IndexError as ie:  # verif. if after the symbol is "i"
            return 0,1
    try:
        a = int(new[:poz])
        b = int(new[poz + 1:-1])  # verif. if before and after the symbol is an integer
    except ValueError as ve:
        return 0, -1

    return a,b
