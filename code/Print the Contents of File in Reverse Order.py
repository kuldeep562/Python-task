
# Q-134. Python Program to Print the Contents of File in Reverse Order

file_name=input("Enter file name: ")
for line in reversed(list(open(file_name))):
    print(line.rstrip())

