
# Q-6 Python Program to Print All Integers that Aren’t Divisible by Either 2 or 3.

a = int(input("Enter any range here: "))
print("The range is:", a)
for i in range(a):
    if i % 2 != 0 and i % 3 != 0:
        print(i, end = " ")

