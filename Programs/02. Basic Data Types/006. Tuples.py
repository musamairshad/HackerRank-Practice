# NAME: MUHAMMAD USAMA
# DIFFICULTY LEVEL: EASY                                               
# Max Score: 10

# Note: This code works on Pypy 3.
n = int(input())
lst = map(int, input().split())
t = tuple(lst)
print(hash(t))