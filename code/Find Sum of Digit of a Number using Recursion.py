
# Q-10 Python Program to Find Sum of Digit of a Number using Recursion.

def recursion(a):
    if a == 0:
        return 0
    else:
        return a % 10 + recursion(a // 10)
b = int(input("Enter any number here: "))
result = recursion(b)
print("The sum of digits of", b, "is", result)

