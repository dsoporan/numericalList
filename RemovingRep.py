from UtilsTest import *

def removing(lsplit, l):
    try:
        ck  = lsplit[2].find("to")
    except IndexError as ie:
        ck = -1
    if ck == -1:
        for i in range(1, len(lsplit)):
            poz = verifying_pos(lsplit[i])
            if poz == -1 or poz >= len(l):
                print("Invalid position")
                return l
            l.pop(poz)
    else:
        i = len(lsplit) - 3
        while i >= 1:
            if lsplit[i + 1] == "to":
                poz1 = verifying_pos(lsplit[i])
                poz2 = verifying_pos(lsplit[i + 2])
                if poz1 == -1 or poz2 == -1 or poz1 >= len(l) or poz2 >= len(l):
                    print("Invalid position")
                    return l
                j = 1
                while j <= poz2 - poz1 + 1:
                    l.pop(poz1)
                    j += 1
            i -= 3


    return l

def replacing(lsplit, l):
    if len(lsplit) == 4:
        if lsplit[2] == "with":
            if verifying(lsplit[1]) == 1:
                old = lsplit[1]
            else:
                return l
            if verifying(lsplit[3]) == 1:
                new = lsplit[3]
            else:
                return l
            i = l.count(old)
            while i > 0:
                k = l.index(old)
                l[k] = new
                i -= 1
    else:
        print("Invalid syntax")
    return l