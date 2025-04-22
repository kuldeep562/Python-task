
# Q-105. Python Program to Count the Occurrences of Each Word in a String
word=input("Enter the word : ").split()
count=0
for i in word:
    count=0
    for j in range(len(word)):
        if i==word[j]:
            count=count+1
    print("Occurance of",i," is :",count) 


