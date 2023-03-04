# NAME: MUHAMMAD USAMA
# DIFFICULTY LEVEL: EASY                                              
# Max Score: 30


# 1st Method

# T = int(input())
# for i in range(T):
#     S = input()
#     lst = []
#     for i in range(len(S)):
#         if(i % 2 == 0):
#             lst.append(S[i])
#             s = "".join(lst)
#     print(s,end=" ")
#     lst = []
#     for i in range(len(S)):
#         if(i % 2 != 0):
#             lst.append(S[i])
#             s = "".join(lst)
#     print(s)




# 2nd Method

T = int(input())
for i in range(T):
    S = input()
    evenCharacters = ""
    oddCharacters = ""
    for i in range(len(S)):
        if(i % 2 == 0):
            evenCharacters += S[i]
        else:
            oddCharacters += S[i]
    print(evenCharacters,oddCharacters)  