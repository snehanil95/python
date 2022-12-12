def main():
    print("enter the number=")
    no=int(input())
    while no!=0 :
        i=no
        for i in range(0,no,1):
            print("*",end=" ")
        no=no-1
        print()



if __name__ == '__main__':
    main()
