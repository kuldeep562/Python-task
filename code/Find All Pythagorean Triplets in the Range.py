
# Q-58. Python Program to Find All Pythagorean Triplets in the Range

limit=int(input("Enter upper limit:"))
c=0
m=2
while(c<limit):
    for n in range(1,m):
        a=m*m-n*n
        b=2*m*n
        c=m*m+n*n
        if(c>limit):
            break
        print(a,b,c)
    m=m+1
