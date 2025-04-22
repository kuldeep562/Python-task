
# Q-114. Python Program to Remove a Key from a Dictionary

d={'Name':'student','Roll_NO':7,'DEPART':'COMPUTER SCIENCE','COUNTRY':'INDIA'}
print("Your current data : ",d)
key=input("Enter the key you want t remove : ")
d.pop(key)
print("New data : ",d)
