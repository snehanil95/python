import pathlib

import os
from sys import *
def directoryWatcher(dname,fext):
    fd=open("logfile.txt","a")
    fdr=open("logfile.txt","r")
    print("Inside directory watcher method")
    #print("Name of input directory : ",Dir_Name)
    #datatypes are list foldername,f..all 3
    for foldername, subfolder, Filenames in os.walk(dname):
        print("")
        for subf in subfolder:
            print(" ")
        for fnames in Filenames:
            if(fnames.endswith(fext)):
                fd.writelines(fnames+"\n")
                
    print(fdr.read())           
                
    fd.close()

        
    
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
