//Duplicate files
from sys import *
import os
import hashlib
def hashfile(path,blocksize=1024):
    afile=open(path,'rb')
    hasher=hashlib.md5()
    buf=afile.read(blocksize)

    while len(buf)>0:
        hasher.update(buf)
        buf=afile.read(blocksize)
    afile.close()

    return hasher.hexdigest()


def DisplayChecksum(Dir_Name):
    #flag=os.path.isabs(path)
    #print(flag)
    
    dups={}
    print("*")
    for foldername, subfolder, Filenames in os.walk(Dir_Name):
        print("**")
        print("Folder name is : "+foldername)
        for subf in subfolder:
            print("Subfolder name of "+foldername+" is "+subf)
        for fnames in Filenames:
            print("File inside folder "+foldername+" is "+fnames)
            path=os.path.join(foldername,fnames)
            file_hash=hashfile(path)

            if file_hash in dups:
                dups[file_hash].append(path)
            else:
                dups[file_hash]=[path]
    #print(dups)
    return dups


def printResult(dict1):
    results=list(filter(lambda x:len(x)>1,dict1.values()))

    if(len(results)>0):
        print("Duplicates found")
        print("following are duplicates files:")

        for result in results:
            for subres in result:
                print("\t\t%s"%subres)

    else:
        print("No duplicates found")



def main():

    print("Automation script started with name:",argv[0])

    if(len(argv)!=2):
        print("Error:Insufficient arguments")
        print("Use -h for help and use -u for usage of script")
        exit()

    if((argv[1]=="-h") or (argv[1]=="-H")):
        print("Help:This script is used to perform ........")
        exit()

    if((argv[1]=="-u")or (argv[1] =="-U")):
        print("Usage:provide___number of argument as")
        print("First Argument as:____")
        print("Secong Argument as:____")
        exit()
    else:
        arr=DisplayChecksum(argv[1])
        printResult(arr)
         




if __name__ =="__main__":
    main()   