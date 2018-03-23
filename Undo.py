def getting_list_undo(l, l_back):
    l_back.append("sep")
    l_back.extend(l)
    return l_back

def del_sep(l_back):
    i = len(l_back) - 1
    j = i
    ok = 0
    while i >= 0:
        if l_back[i] == "sep":
            ok = 1
            break
        i -= 1
    k = j - i
    while k >= 0 and len(l_back) != 0 and ok == 1:
        l_back.pop()
        k -= 1
    return l_back

def check(l_back):
    for i in range(len(l_back)):
        if l_back[i] == "sep":
            return True
    return False

def resign_list_undo(l_back):
    new = []
    i = len(l_back) - 1
    while i >= 0:
        if l_back[i] == "sep":
            break
        i -= 1
    poz = i
    i -= 1
    while i >= 0:
        if l_back[i] == "sep":
            break
        new.append(l_back[i])
        i -= 1
    l_back = del_sep(l_back)
    new.reverse()
    return new
