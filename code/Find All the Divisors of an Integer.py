
# Q-13 Python Program to Find All the Divisors of an Integer.

list_of_divisors = []
a = int(input("Enter any range here: "))
print("The number is:", a)
for i in range(1, a + 1):
    if a % i == 0:
        list_of_divisors.append(i)
print("The divisors are",list_of_divisors)

