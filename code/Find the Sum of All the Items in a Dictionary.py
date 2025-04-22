
# Q-112. Python Program to Find the Sum of All the Items in a Dictionary

x={}
n=int(input("Enter the no. of entries you want : "))
for i in range(n):
      name=input("Enter the name : ")
      marks=int(input("Enter the marks : "))
      x.update({name:marks})
count=0
for i in x:
    count=count+x[i]
print("Total marks :",count) 
