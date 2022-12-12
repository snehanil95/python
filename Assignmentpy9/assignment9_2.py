from sys import *

fd1=open(argv[1],"r")
line=fd1.readline()
print("file content are:")
while(line!=""):
    print(line)
    line=fd1.readline()

fd1.close()
