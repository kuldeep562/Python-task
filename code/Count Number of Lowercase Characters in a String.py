
# Q-90. Python Program to Count Number of Lowercase Characters in a String

string=input("Enter string:")
count=0
for i in string:
      if(i.islower()):
            count=count+1
print("The number of lowercase characters is:")
print(count)


