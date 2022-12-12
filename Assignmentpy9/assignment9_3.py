
from sys import *
fdr=open(argv[1],"r")
fdw=open("Demo.txt","a")

for i in fdr:
    fdw.write(i)