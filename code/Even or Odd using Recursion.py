
# Q-1 Python Program to Check Whether a Given Number is Even or Odd using Recursion.

def even(number):
    if number == 0:
        return True
    elif number == 1:
        return False
    else:
        return even(number - 2)

def odd(number):
    return not even(number)

a = int(input("Enter any number here: "))
if even(a):
    print(a, "is not an odd number..")
    print(a, "is even number..")
else:
    print(a, "is not an even number..")
    print(a, "is odd number..")

