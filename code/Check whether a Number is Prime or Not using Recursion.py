
# Q-26. Python Program to Check whether a Number is Prime or Not using Recursion

def check(n, div = None):
    if div is None:
        div = n - 1
    while div >= 2:
        if n % div == 0:
            print("Number not prime")
            return False
        else:
            return check(n, div-1)
    else:
        print("Number is prime")
        return 'True'
n=int(input("Enter number: "))
check(n)
