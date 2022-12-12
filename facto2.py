def main() :
    print("Enter the number:")
    no=int(input())

    print("factors are:")
    for i in range(1,int(no/2)+1,1):
        if no%i==0:
            print(i)
        #i=i+1



if __name__=="__main__":
    main()