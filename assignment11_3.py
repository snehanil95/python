from sys import *
import os
import hashlib
import time
def Deletefiles(dict1):
    print(dict1)
    results=list(filter(lambda x:len(x)>1,dict1.values()))

    iCnt=0

    if(len(results)>0):
        for result in results:
            for subresult in result:
                iCnt+=1
                if iCnt>=2:
                    os.remove(subresult)
        iCnt=0
    else:
        print("No duplicate found")
        

def hashfile(path,blocksize=1024):
    afile=open(path,'rb')
    hasher=hashlib.md5()
    buf=afile.read(blocksize)

    while len(buf)>0:
        hasher.update(buf)
        buf=afile.read(blocksize)
    afile.close()

    return hasher.hexdigest()

def findDup(path):
    flaf=os.path.isabs(path)

    if flag==false:
        path=os.path.abspath(path)

    exists=os.path.isdir(path)

    dups={}

    if exists:
        for dirName,sundirs,fileList in os.walk(path):
            print("Current folder :"+dirName)
            for filen in fileList:
                path=os.path.join(dirName,filen)
                file_hash=hashfile(path)

                if file_hash in dups:
                    dups[file_hash].append(path)
                else:
                    dups[file_hash]=[path]

        return dups

    else:
        print("Invalid path")


def printResult(dict1):
    separator="-"*80

    fd=open("DupsFile%s.log"%(time.ctime()),'a')
    fd.write(separator+"\n")
    fd.write("Duplicates files:")
    fd.write("\n"+separator+"\n")
    results=list(filter(lambda x:len(x)>1,dict1.values()))

    if len(results)>0:
        #print("Duplicates found")
        #f.write("the following are duplicates:")

        for result in results:
            for subresult in result:
                fd.writelines('\t\t%s'%subresult)

    else:
        fd.write("No duplicates found")

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
startt=time.time()
fd=open("DupFile","a")
arr=DisplayChecksum(argv[1]) 
fd.writelines(arr)
printResult(arr)
Deletefiles(arr)
endtime=time.time()
print("Time %s took for execution:"%(endtime-startt))
#print(arr)            