import os

def ReadFile(fname):
    if(os.path.exists(fname)):
        

        fd=open(fname,"r")
        Data=fd.read()
        print(Data)

        fd.close()

    else:
        print("file is not exist")
        return




def main():
    print("Enter teh file name to create:")
    Name=input()


    ReadFile(Name)





if __name__ =="__main__":
    main()