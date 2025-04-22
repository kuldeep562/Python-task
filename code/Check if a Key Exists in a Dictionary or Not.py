
# Q-110. Python Program to Check if a Key Exists in a Dictionary or Not

x={}
n=int(input("Enter the no. of entries you want : "))
for i in range(n):
      name=input("Enter the name : ")
      marks=int(input("Enter the marks : "))
      x.update({name:marks})
key=input("Enter the key to check : ")
if key in x:
      print("yes")
else:
      print("not exist")

