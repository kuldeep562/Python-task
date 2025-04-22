
# Q-106. Python Program to Count Number of Vowels in a String using Sets

vowel={'a','u','i','e','o'}
word=input("Enter the word : ")
count=0
for i in word:
    if i in vowel:
        count=count+1
print("No. of vowels are : ",count)  

