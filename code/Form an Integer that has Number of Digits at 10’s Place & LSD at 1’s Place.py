
# Q-65. Python Program to Form an Integer that has Number of Digits at 10’s Place & LSD at 1’s Place

n=int(input("Enter the number:"))
tmp=n
k=0
while(n>0):
    k=k+1
    n=n//10
b=str(tmp)
c=str(k)
d=c+b[k-1]
print("The new number formed:",int(d))

