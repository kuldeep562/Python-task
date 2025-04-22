
# Q-7 Python Program to Find Numbers which are Divisible by 7 and Multiple of 5 in a Given Range.

a = int(input("Enter any range here: "))
print("The range is:", a)
for i in range(a):
    if i % 7 == 0 and i % 5 == 0:
        print(i, end = " ")

