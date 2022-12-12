def prime(no):
    for i in range(2,int(no/2)+1,1) :
        if(no%i==0):
            return 1
            exit()
        else:
            return 0





def main():
    print ("enter the number to check prime or not=")
    no=int(input())
    flag=prime(no)

    if(flag==1):
        print("number is not prime")

    else:
        print("number is prime")


if __name__=="__main__":
    main()