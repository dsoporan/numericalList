from UtilsTest import *
from Adding import *
from RemovingRep import *
from PrintingMod import *
from SumProduct import *
from Filtering import *
from Undo import *
from Testing import *

def reading():
    l = ['3+2i', '3+2i', '4+55i', '2+5i', '33+2i', '66+22i', '13+2i', '132+3i', '222+11i', '3+2i', '3+2i', '5+2i', '3+7i', 'i']
    l_back = []
    l_back.extend(l)
    check2 = []
    check2.extend(l)
    while True:
        new = input("Command::::::")
        poz = new.find("  ")
        while poz != -1:
            new = new[:poz] + new[poz + 1:]
            poz = new.find("  ")
        lsplit = new.split(" ")
        if lsplit[0] == "add":
            l = adding(lsplit, l)
            l_back = getting_list_undo(l, l_back)
        elif lsplit[0] == "insert":
            l = inserting(lsplit, l)
            l_back = getting_list_undo(l, l_back)
        elif lsplit[0] == "remove":
            l = removing(lsplit, l)
            l_back = getting_list_undo(l, l_back)
        elif lsplit[0] == "replace":
            l = replacing(lsplit, l)
            l_back = getting_list_undo(l, l_back)
        elif lsplit[0] == "list":
            if len(lsplit) == 1:
                print(l)
            elif len(lsplit) == 5:
                if lsplit[1] == "real" and lsplit[3] == "to":
                     printing_real(lsplit, l)
            elif len(lsplit) == 4:
                if lsplit[1] == "modulo":
                    if lsplit[2] == "<" or lsplit[2] == ">" or lsplit[2] == "=":
                        pos = verifying_pos(lsplit[3])
                        if pos != -1:
                            lis = modulos(l)
                            if len(lis) != 0:
                                printing_mod(l, lis, lsplit[2], pos)
                            else:
                                print("None")
            else:
                print("Invalid syntax")
        elif lsplit[0] == "sum" and lsplit[2] == "to":
            poz1 = verifying_pos(lsplit[1])
            poz2 = verifying_pos(lsplit[3])
            if poz1 != -1 and poz2 != -1:
                if poz1 < poz2 and poz1 < len(l) and poz2 < len(l):
                    print(sum_pos(poz1, poz2, l))
        elif lsplit[0] == "product" and lsplit[2] == "to":
            poz1 = verifying_pos(lsplit[1])
            poz2 = verifying_pos(lsplit[3])
            if poz1 != -1 and poz2 != -1:
                if poz1 < poz2 and poz1 < len(l) and poz2 < len(l):
                    print(product_pos(poz1, poz2, l))
        elif lsplit[0] == "filter":
            if lsplit[1] == "real":
                l = filtering_real(l)
                l_back = getting_list_undo(l, l_back)
            elif lsplit[1] == "modulo":
                if lsplit[2] == "<" or lsplit[2] == ">" or lsplit[2] == "=":
                    l = filtering_modulos(l, lsplit[2], lsplit[3])
                    l_back = getting_list_undo(l, l_back)
        elif lsplit[0] == "undo":
            if check2 == l:
                print("No more UNDO")
            elif check(l_back) == True:
                l = resign_list_undo(l_back)
        else:
            print("Exiting")
            break

def main():
    reading()
    #test_all()

main()
