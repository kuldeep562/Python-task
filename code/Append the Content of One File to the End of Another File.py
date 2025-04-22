
# Q-135. Python Program to Append the Content of One File to the End of Another File

file1 = input("Enter file to be read from: ")
file2 = input("Enter file to be appended to: ")
fin = open(file1, "r")
data2 = fin.read()
fin.close()
fout = open(file2, "a")
fout.write(data2)
fout.close()



