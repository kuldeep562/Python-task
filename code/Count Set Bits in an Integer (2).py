
# Q-61. Python Program to Count Set Bits in an Integer

def countsetbits(A):
    count = 0       
    while(A!=0):
        A = A & (A-1)    
        count = count+1  
    return(count)       
 
n = int(input("Enter the Number: "))
print(countsetbits(n))

