
# Q-25 Python Program to Check Prime Number.

a = int(input("Enter any number here: "))
if a > 1:
    for i in range(2, int(a/2)):
        if(a % i == 0):
            print(a,"is not a prime number")
            break
    else:
        print(a,"is a prime number")
else:
    print(a,"is not a prime number")
 
