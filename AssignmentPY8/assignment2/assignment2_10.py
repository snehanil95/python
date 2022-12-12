def main():
    print("enter the number")
    no=int(input())
    sum=0
    while ( no>0) :
        no1=int(no%10)
        sum=sum+no1
        no=no/10
    print(sum)




if __name__ =="__main__":
    main()