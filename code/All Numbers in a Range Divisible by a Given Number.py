
# Q-8 Python Program to Print All Numbers in a Range Divisible by a Given Number.

a = int(input("Enter any range here: "))
print("The range is:", a)
n = int(input("Enter a number which divides a number of given range: "))
print("The number is:", n)
for i in range(1,a):
    if i % n == 0:
        print(i, end = " ")
