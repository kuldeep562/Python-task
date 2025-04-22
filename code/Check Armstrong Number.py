
# Q-28 Python Program to Check Armstrong Number

a = int(input("Enter any number here: "))
convert_str = str(a)
a_len = len(convert_str)
sum_of = sum(int(digit) ** a_len for digit in convert_str)
if sum_of == a:
    print(a,"is an Armstrong number..")
else:
    print(a,"is not an Armstrong number..")
