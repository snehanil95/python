import os

def WriteFile(fname):
    if(os.path.exists(fname)):
        print("Enter thedata to write in file")
        Data=input()

        fd=open(fname,"a")
        fd.write(Data)

    else:
        print("file is not exist")
        return




def main():
    print("Enter teh file name to create:")
    Name=input()


    WriteFile(Name)





if __name__ =="__main__":
    main()