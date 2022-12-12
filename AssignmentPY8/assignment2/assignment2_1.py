def addnum(A,B):
            sum=A+B
            print("addition is",sum)


def subnum(A, B):
    sub = A - B
    print("substraction is", sub)


def divnum(A, B):
    (div) = float(A / B)
    print("division is", (div))


def multnum(A, B):
    mult= A * B
    print("multiplication is", mult)

def main():
    print("enter the two number=")
    no1=int(input())
    no2=int(input())

    print("which arithmatic operation you want to perform on that number=")
    print("add,sub,div,mult choose any one")
    opr=input()

    if(opr=='add'):
        addnum(no1,no2)
        exit()
    if(opr=='sub'):
        subnum(no1,no2)
        exit()
    if (opr == 'div'):
        divnum(no1, no2)
        exit()
    if (opr == 'mult'):
        multnum(no1, no2)
        exit()

    else :
        print("invalid operation")
        exit()


if __name__ =="__main__":
    main()