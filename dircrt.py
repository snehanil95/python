import os
from sys import *
def directoryWatcher(dname):
    print("Inside directory watcher method")
    print("Name of input directory : ",Dir_Name)
    #datatypes are list foldername,f..all 3
    for foldername, subfolder, Filenames in os.walk(Dir_Name):
        print("Folder name is : "+foldername)
        for subf in subfolder:
            print("Subfolder name of "+foldername+" is "+subf)
        for fnames in Filenames:
            print("File inside folder "+foldername+" is "+fnames+"having size"+os.path.getsize(fname))
        print(" ")
    
def main():
    if(argv[1]=="-h"):
        print("script will travel the directory and display name of alll entry")
        exit()
    if(argv[1]=="-u"):
        print(".usage...")
        exit()

    if(len(argv)!=2):
        print("insufficient argument")

    directoryWatcher(argv[1])

if __name__=="__main__":
    main()