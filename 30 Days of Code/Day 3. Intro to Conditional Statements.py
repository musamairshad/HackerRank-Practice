# NAME: MUHAMMAD USAMA
# DIFFICULTY LEVEL: EASY                                              
# Max Score: 30


if (__name__) == '__main__':
    N = int(input().strip())
    if(N % 2 != 0):
        print("Weird")
    elif (N % 2 == 0 and 2 <= N <= 5):
        print("Not Weird")
    elif (N % 2 == 0 and 6 <= N <= 20):
        print("Weird")
    elif (N % 2 == 0 and N > 20):
        print("Not Weird")