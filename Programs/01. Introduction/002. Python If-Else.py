# NAME: MUHAMMAD USAMA
# DIFFICULTY LEVEL: EASY                                               
# Max Score: 10

# # 1st Method:

# no = int(input("Enter number: "))
# if(no % 2 != 0):
#     print("Weird")
# elif (no % 2 == 0 and 2 <= no <= 5):
#     print("Not Weird")
# elif (no % 2 == 0 and 6 <= no <= 20):
#     print("Weird")
# elif (no % 2 == 0 and no > 20):
#     print("Not Weird")


# 2nd Method:

no = int(input("Enter number: "))
if(n % 2 != 0 or (n % 2 == 0 and 6 <= n <= 20)):
    print("Weird")
else:
    print("Not Weird")