
# Q-62. Python Program to Clear the Rightmost Set Bit of a Number

def fun(n):
    return n & (n-1)


n = int(input("enter a number"))
print("The number after unsetting the rightmost set bit", fun(n))
