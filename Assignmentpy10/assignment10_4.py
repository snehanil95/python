#not working
import shutil
from sys import *
import os



def directoryWatcher(src,dst,ext):
    for foldername, subfolder, Filenames in os.walk(src):
        
        for fnames in Filenames:
            if(fnames.endswith(ext)):
                pathname=os.path.join(src,fnames)
                if os.path.isfile(pathname):
                    shutil.copy(pathname,dst)
    


    


def main():
    if(argv[1]=="-h"):
        print("script will travel the directory and display name of alll entry")
        exit()
    if(argv[1]=="-u"):
        print(".usage...")
        exit()

    if(len(argv)!=4):
        print("insufficient argument")

    directoryWatcher(argv[1],argv[2],argv[3])

if __name__=="__main__":
    main()
