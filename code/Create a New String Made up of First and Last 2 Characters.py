
# Q-101. Python Program to Create a New String Made up of First and Last 2 Characters

word=input("Enter the word : ")
news=""
for i in range(0,len(word)):
    if i==0:
        news=news + word[i]
    elif i==len(word)-2:
        news=news + word[i]
    elif i==len(word)-1:
        news=news + word[i]
print("NEW STRING : ",news)
