
# Q-18 Python Program to Calculate Grade of a Student.

a = float(input("Enter the marks of a student: "))
total_marks = float(input("Enter total marks here: "))
print("The Marks is:",a)
print("The Total Marks is:",total_marks)
per = (a / total_marks) * 100
print(per)
if per <= 100 and per >= 85:
    print("A student achieve A grade..")
elif per <= 84 and per >= 70:
    print("A student achieve B grade..")
elif per <= 69 and per >= 55:
    print("A student achieve C grade..")
elif per <= 54 and per >= 40:
    print("A student achieve D grade..")
else:
    print("A student need to work hard..!!")

