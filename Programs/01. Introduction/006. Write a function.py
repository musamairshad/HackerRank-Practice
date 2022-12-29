# NAME: MUHAMMAD USAMA
# DIFFICULTY LEVEL: MEDIUM                                               
# Max Score: 10

# 1st Method:

# def is_leap(year):
#     leap = False
#     if(year % 4 == 0):
#         if(year % 100 == 0):
#             if(year % 400 == 0):
#                 leap = True
#             else:
#                 leap = False
#         else:
#             leap = True
#     else:
#         leap = False
                
#     return leap

# year = int(input("Enter any year to check: "))
# print(is_leap(year))


# 2nd Method:

def is_leap(year):
    return (year % 4 == 0) and (year % 100 != 0 or year % 400 == 0)

year = int(input("Enter any year to check: "))
print(is_leap(year))