
# Q-43. Python Program to Find the Factorial of a Number using Recursion.

def factorial(n):
    if(n <= 1):
        return 1
    else:
        return(n*factorial(n-1))
n = int(input("Enter number:"))
print("Factorial of a Number is:")
print(factorial(n))
