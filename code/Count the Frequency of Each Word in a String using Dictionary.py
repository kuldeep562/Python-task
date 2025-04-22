
# Q-119. Python Program to Count the Frequency of Each Word in a String using Dictionary

string=input("Enter the string : ").split()
count=[string.count(i) for i in string]
d=dict(zip(string,count))
print(d)
