# NAME: MUHAMMAD USAMA
# DIFFICULTY LEVEL: EASY
# Max Score: 10

n = int(input())
A = set(map(int, input().split()))
b = int(input())
B = set(map(int, input().split()))
AUB = A | B
print(len(AUB))