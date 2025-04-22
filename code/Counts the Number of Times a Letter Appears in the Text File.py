
# Q-132. Python Program to Counts the Number of Times a Letter Appears in the Text File

file_name = input("Enter file name: ")
l=input("Enter letter to be searched:")
k = 0
 
with open(file_name, 'r') as f:
    for line in f:
        words = line.split()
        for i in words:
            for letter in i:
                if(letter==l):
                    k=k+1
print("Occurrences of the letter:")
print(k)
