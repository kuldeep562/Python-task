
# Q-14 Python Program to Find the Smallest Divisor of an Integer.

a = int(input("Enter any range here: "))
print("The number is:", a)
for i in range(2, a):
    if a % i == 0:
        print("The smallest divisor is:", i)
        break
