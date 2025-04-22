
# Q-103. Python Program to Swap the First and the Last Character of a String

word=input("Enter the word : ")
x=list(word)
temp = x[0]
x[0]=x[-1]
x[-1]=temp
print(''.join(x))
