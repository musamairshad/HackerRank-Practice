# NAME: MUHAMMAD USAMA
# DIFFICULTY LEVEL: EASY                                               
# Max Score: 10

n = int(input())
arr = map(int, input().split())
s = sorted(set(arr))
lst = list(s)
max = lst[0]
for i in range(len(lst)):
    if(max < lst[i]):
        max = lst[i]
lst.remove(max)
print(lst[-1])