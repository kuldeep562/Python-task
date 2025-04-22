
# Q-102. Python Program to Find the Larger String without using Built-in Functions

word=input("Enter the word : ")
word=word.split()
count=0
li=[]
for i in word:
    if len(i)>=count:
        li=[]
        li.append(i)
        count=len(i)
print("Largest string : ",li)

