
# Q-107. Python Program to Check if a Given String is Palindrome

for i in range(2):
    n=input("Enter your word : ")
    a=[]
    for i in n:
        a.append(i)
    a.reverse()
    a=''.join(a)
    if (a==n):
        print("It is palindrome\n")
    else :
        print("No it is not a palidrome\n")

