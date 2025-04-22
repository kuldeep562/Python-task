
# Q-44. Python Program to Find the Factorial of a Number Without Recursion.

n=int(input("Enter number:"))
fact=1
while(n>0):
    fact=fact*n
    n=n-1
print("Factorial of the number is: ")
print(fact)

