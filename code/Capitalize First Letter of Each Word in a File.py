
# Q-131. Python Program to Capitalize First Letter of Each Word in a File

file_name = input("Enter file name: ")
 
with open(file_name, 'r') as f:
    for line in f:
        l=line.title()
        print(l)




