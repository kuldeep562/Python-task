
# Q-155. Python Program to Find the Cumulative Sum of a List

list=[10,200,30,450,50]
new_list=[] 
j=0
for i in range(0,len(list)):
    j+=list[i]
    new_list.append(j) 
     
print(new_list) 
