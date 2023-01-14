# NAME: MUHAMMAD USAMA
# DIFFICULTY LEVEL: EASY                                               
# Max Score: 10

def mutate_string(string, position, character):
    lst = list(string)
    lst[position] = character
    s = "".join(lst)
    return s