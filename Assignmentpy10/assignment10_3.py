import shutil
from sys import *


def directoryWatcher(src,dst):
    shutil.copytree(src,dst)



    


def main():
    if(argv[1]=="-h"):
        print("script will travel the directory and display name of alll entry")
        exit()
    if(argv[1]=="-u"):
        print(".usage...")
        exit()

    if(len(argv)!=3):
        print("insufficient argument")

    directoryWatcher(argv[1],argv[2])

if __name__=="__main__":
    main()
