
# Q-9 Python Program to Find Sum of Digits of a Number.

a = int(input("Enter any number here: "))
print("The number is: ",a)
convert_str = str(a)
sum = 0
for i in map(int,convert_str):
    sum = sum + i 
print("The sum of digits of a number is: ",sum)


