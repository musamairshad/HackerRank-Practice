# NAME: MUHAMMAD USAMA
# DIFFICULTY LEVEL: EASY
# Max Score: 10

# Www.HackerRank.com → wWW.hACKERrANK.COM

def swap_case(s):
    lst = list(s)
    for i in range(len(lst)):
        if (lst[i].islower()):
            lst[i] = lst[i].upper()
        else:
            lst[i] = lst[i].lower()
    s = "".join(lst)
    return s
