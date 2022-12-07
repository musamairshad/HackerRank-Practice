# NAME: MUHAMMAD USAMA
# DIFFICULTY LEVEL: EASY                                               DATE: 07-DEC-2022
# Max Score: 10

no = int(input("Enter number: "))
if(no % 2 != 0):
    print("Weird")
elif (no % 2 == 0 and 2 <= no <= 5):
    print("Not Weird")
elif (no % 2 == 0 and 6 <= no <= 20):
    print("Weird")
elif (no % 2 == 0 and no > 20):
    print("Not Weird")