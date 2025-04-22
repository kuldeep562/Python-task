
# Q-12 Python Program to Count the Number of Digits in a Number.

a = int(input("Enter any number here: "))
print("The number is:",a)
convert_str = str(a)
count = 0
for i in map(int, convert_str):
    count = count + 1
print("Total numbers of digit in given number is ",count)

