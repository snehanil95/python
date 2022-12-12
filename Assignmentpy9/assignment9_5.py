
from sys import *

def woldCount(fname,str1):
    cnt=0
    fd=open(fname,'r')
    for line in fd:
        
        
        words=line.split()

        for wd in words:
            if(wd==str1):
                cnt=cnt+1
        
            
    
    return cnt

print("Number of words:",argv[1],"is",woldCount(argv[1],argv[2]))