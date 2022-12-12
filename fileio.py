import os

def crtfile(fname):

    if(os.path.exists(fname)):
        print("file exists")
        return
    else:

        fd=open(fname,"w")



def main():
    print("Enter teh file name to create:")
    Name=input()


    crtfile(Name)





if __name__ =="__main__":
    main()