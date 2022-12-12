from sys import *
import os
import hashlib
import time

def Deletefiles(dict1):
    result=list(filter(lambda X:len(X)>1),dict1.values())

    iCnt=0

    if len(results)>0:
        for result in results:
            for subresult in result:
                iCnt+=1
                if iCnt>=2:
                    os.remove(subresult)
            iCnt=0

    else:
        print("No duplicates file found:")




def hashfile(path,blocksize=1024):
    afile=open(path,'rb')

    hasher=hashlib.md5()
    buf=afile.read(blocksize)

    while(len(buf)>0):
        hasher.update(buf)
        buf=afile.read(blocksize)

    afile.close()

    return hasher.hexdigest()


def findDups(path):
    flag=os.path.isabs(path)

    exists=os.path.isdir(path)

    dup={}

    if exists:
        for Dname,SubD,fileList in os.walk(path):
            print("Current folder is:",Dname)

            for fileN in fileList:
                path=os.path.join(Dname,fileN)
                file_hash=hashfile(path)

                if file_hash in dups:
                    dups[file_hash].append(path)

                else:
                    dups[file_hash]=path

        return dups
    
    else:
        print("Invalid path")

def printResult(dict1):
    results=list(filter(lambda x:len(x)>1,dict1.values))

    if(len(result)>0):
        print("Duplicates found")
        print("following are duplicates files:")

        for result in results:
            for subres in result:
                print("\t\t %s"%subresult)

    else:
        print("No duplicates found")

def main():
    if(len(argv)!=2):
        print("Invalid number of arguments")
        exit()

    if((argv[1]=='-h')and(argv[1]=='-H')):
        print("help:")
        exit()

    if((argv[1]=='-u')and(argv[1]=='-U')):
        print("Usage:")
        exit()


    try:
        arr={}
        StartT=time.time()
        arr=findDups(argv[1])
        printResult(arr)
        Deletefiles(arr)
        EndT=time.time()

        print("Time took for execution%s"%(EndT-StartT))

    except ValueError:
        print("Error:Invalide datatype")


    except Exception as E:
        print("Error:Invalide Input")

    

if __name__=="__main__":
    main()
            