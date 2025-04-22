
# Q-133. Python Program to Extract Numbers from Text File

file_name = input("Enter file name: ")
 
with open(file_name, 'r') as f:
    for line in f:
        words = line.split()
        for i in words:
            for letter in i:
                if(letter.isdigit()):
                    print(letter)
