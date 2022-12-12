from sys import *
import pathlib
file = pathlib.Path(argv[1])
if file.exists ():
    print ("File exist")
else:
    print ("File not exist")

