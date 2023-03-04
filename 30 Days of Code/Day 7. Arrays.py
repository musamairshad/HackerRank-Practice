# NAME: MUHAMMAD USAMA
# DIFFICULTY LEVEL: EASY                                              
# Max Score: 30


if __name__ == '__main__':
    n = int(input().strip())
    arr = list(map(int, input().rstrip().split()))
    for i in reversed(range(len(arr))):
        print(arr[i],end=" ")