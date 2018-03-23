from UtilsTest import *
from Adding import *
from RemovingRep import *
from PrintingMod import *
from SumProduct import *
from Filtering import *

def test_adding():
    l = ["1","2","3"]
    lsplit = ["4","5","6"]
    assert adding(lsplit,l) == ["1","2","3","5","6"]
    lsplit = ["add"]
    assert adding(lsplit,l) == l
    lsplit = []
    assert adding(lsplit,l) == l

def test_inserting():
    l = ["1","2","3"]
    lsplit = ["insert","5","at", "0"]
    assert inserting(lsplit,l) == ["5","1","2","3","5","6"]
    lsplit = ["insert", "11", "at", "1", "12", "at", "2"]
    assert insert(lsplit,l) == ["1", "11", "12", "2", "3"]
    lsplit = []
    assert adding(lsplit,l) == l

def test_removing():
    l = ["1","2","3","4","5","6"]
    lsplit = ["remove", "0","0","0"]
    assert removing(lsplit,l) == ["4","5","6"]
    lsplit = ["remove", "1", "2"]
    l = ["1", "2", "3", "4", "5", "6"]
    assert removing(lsplit,l) == ["1", "3", "5", "6"]
    lsplit = ["remove", "2"]
    assert removing(lsplit,l) == ["1", "3", "6"]

def test_replacing():
    l = ["3", "2", "3", "4", "5", "3"]
    lsplit = ["replace", "3", "with", "0"]
    assert replacing(lsplit, l) == ["0", "2", "0", "4", "5", "0"]
    lsplit = ["replace", "0", "with", "22"]
    assert replacing(lsplit, l) == ["22", "2", "22", "4", "5","22"]
    lsplit = ["replace", "1", "with", "0"]
    assert replacing(lsplit, l) == ["22", "2", "22", "4", "5","22"]

def test_modulos():
    l = ["3", "2", "3", "4", "5", "3"]
    assert modulos(l) == [3, 2, 3, 4, 5, 3]
    l = ["3", "0", "0", "4", "5", "5"]
    assert modulos(l) == [3, 0, 0, 4, 5, 5]

def test_sum_pos():
    l = ["1+2i", "3", "4+2i", "-3+2i", "2"]
    assert sum_pos(0, 3, l) == complex(5, 6)
    assert sum_pos(2, 3, l) == complex(1, 4)

def test_product_pos():
    l = ["1+2i", "3", "4+2i", "-3+2i", "2"]
    assert product_pos(0, 3, l) == complex(-60, -90)
    assert product_pos(2, 3, l) == complex(-16, 2)

def test_filter_real():
    l = ["1+2i", "3", "4+2i", "-3+2i", "2"]
    assert filtering_real(l) == ["3", "2"]
    l = ["1+2i", "3+i", "4+2i", "-3+2i", "-2i"]
    assert filtering_real(l) == []

def test_filtering_modulos():
    l = ["2i", "3", "4", "-1+2i", "2"]
    assert filtering_modulos(l, "<", 10) == ["2i", "3", "4", "-1+2i", "2"]
    l = ["2", "3", "4", "2", "2"]
    assert filtering_modulos(l, "=", 2) == ["2", "2", "2"]
    l = ["2+2i", "3", "4", "2", "2"]
    assert filtering_modulos(l, ">", 2) == ["2+2i", "3", "4"]

def test_verifying_pos():
    assert verifying_pos("55") == 55
    assert verifying_pos("5555") == 5555
    assert verifying_pos("-1255") == -1255

def test_verifying():
    assert verifying("55+2i") == 1
    assert verifying("5555") == 1
    assert verifying("-1255+ni") == -1

def test_real_imaginary():
    assert real_imaginary("5+2i") == (5, 2)
    assert real_imaginary("-i") == (0,-1)
    assert real_imaginary("-1255") == (-1255, 0)

def test_all():
    print(test_adding())
    print(test_adding())
    print(test_removing())
    print(test_replacing())
    print(test_modulos())
    print(test_sum_pos())
    print(test_product_pos())
    print(test_filter_real())
    print(test_filtering_modulos())
    print(test_verifying_pos())
    print(test_verifying())
    print(test_real_imaginary())