def facto(A):
    for i in range(1,A,1):
        if(A%i==0):
            print(i)


def main():
    print("enter the number=")
    no1=int(input())

    print("factorial of number=")
    facto(no1)


if __name__=="__main__":
    main()