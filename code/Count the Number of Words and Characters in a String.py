
# Q-89. Python Program to Count the Number of Words and Characters in a String

string=input("Enter string:")
char=0
word=1
for i in string:
      char=char+1
      if(i==' '):
            word=word+1
print("Number of words in the string:")
print(word)
print("Number of characters in the string:")
print(char)

