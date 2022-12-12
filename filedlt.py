import os

def DeleteFile(fname):
    if(os.path.exists(fname)):
        size=os.path.getsize(fname)

        if(size==0):
            os.remove(fname)
            print("File deleted successfully")
        else:
            print("Are you sure to detele file: Y/N")
            op=input()
            if(op=="Y" or op=="y"):
                os.remove(fname)
                print("File deleted successfully")
            else:
                print("file deleted process stopped.")

    else:
        print("file is not exist")
        return




def main():
    print("Enter teh file name to delete:")
    Name=input()


    DeleteFile(Name)





if __name__ =="__main__":
    main()