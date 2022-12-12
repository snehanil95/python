import filecmp
from sys import *

Ret=filecmp.cmp(argv[1],argv[2])

if(Ret==True):
    print("files are exact same")

else:
    print("Files are not same")