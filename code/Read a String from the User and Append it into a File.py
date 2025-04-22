
# Q-136. Python Program to Read a String from the User and Append it into a File

file_name = input("Enter file name: ")
file3=open(file_name,"a")
c=input("Enter string to append: \n");
file3.write("\n")
file3.write(c)
file3.close()
print("Contents of appended file:");
file4=open(file_name,'r')
line1=file4.readline()
while(line1!=""):
    print(line1)
    line1=file4.readline()    
file4.close()

