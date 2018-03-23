from UtilsTest import *

def adding(lsplit, l):
    for i in range(1, len(lsplit)):
        if verifying(lsplit[i]) == -1:
            return l
        l.append(lsplit[i])

    return l

def inserting(lsplit, l):
    if len(lsplit) == 4:
        if verifying(lsplit[1]) == -1:
            return l
        if lsplit[2] == "at":
            poz = verifying_pos(lsplit[3])
            if poz == -1:
                return l
            if poz < len(l):
                l.insert(poz, lsplit[1])
            else:
                print("Invalid position, ")
    else:
        print("Invalid syntax")

    return l