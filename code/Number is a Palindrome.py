
# Q-4 Python Program to Check if a Number is a Palindrome

a = int(input("Enter any number here: "))
convert_str = str(a)
if convert_str == convert_str[::-1]:
    print("The number", a, "is a palindrome")
else:
    print("The number", a, "is not a palindrome")
