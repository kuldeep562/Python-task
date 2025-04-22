
# Q-27 Python Program to Check Whether a Given Number is Perfect Number.

a = int(input("Enter any number here: "))
if a <= 0:
    print("Enter a positive number..")
else:
    sod = 0     #sum of divisors
    for i in range(1,a):
        if a % i == 0:
            sod = sod + i
    if sod == a:
        print(a,"is a perfect number..")
    else:
        print(a,"is not a perfect number..")


