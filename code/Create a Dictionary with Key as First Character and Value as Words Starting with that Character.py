
# Q-117. Python Program to Create a Dictionary with Key as First Character and Value as Words Starting with that Character

x={}
char=["r","y","v","h"]
name=["vishal","raj","yadav","harsh"]
for i in char:
    for j in name:
        if i==j[0]:
            x.update({i:j})
print(x)    

