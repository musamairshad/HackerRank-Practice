# NAME: MUHAMMAD USAMA
# DIFFICULTY LEVEL: EASY                                               
# Max Score: 10

n = int(input("Enter number of students: "))
student_marks = {}
for i in range(n):
    name, *score = input().split()
    scores = list(map(float, score))
    student_marks[name] = scores
query_name = input()
for i in student_marks:
    if(student_marks[i] == query_name):
        sum = 0
        for i in range(len(student_marks[name])):
            sum += student_marks[name][i]
            avg = sum / len(student_marks[name])
    print("%.2f" % avg)
            
            
        
# if(query_name in student_marks):
#     sum = 0
#     for i in range(len(student_marks[name])):
#         sum += student_marks[name][i]
#         avg = sum / len(student_marks[name])
#     print("%.2f" % avg)