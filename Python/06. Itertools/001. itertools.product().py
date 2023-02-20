# NAME: MUHAMMAD USAMA
# DIFFICULTY LEVEL: EASY
# Max Score: 10

from itertools import product

A = map(int, input().split())
B = map(int, input().split())
print(" ".join(map(str, product(A, B))))