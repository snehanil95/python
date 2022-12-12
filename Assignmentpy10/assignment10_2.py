from pathlib import *

import os
from sys import *
def directoryWatcher(dname,oldext,newext):
    fd=open("logfile1.txt","a")
    fdr=open("logfile1.txt","r")
    
    for foldername, subfolder, Filenames in os.walk(dname):
        
        for fnames in Filenames:
            if(fnames.endswith(oldext)):
                fnames=fnames.replace(oldext,newext)

            		
                #base = os.path.splitext(fnames)
                #p=path(fnames)
                #fnames=os.rename(oldext,newext)
                fd.writelines(fnames)
                
    print(fdr.read())           
                
    fd.close()

        
    
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
