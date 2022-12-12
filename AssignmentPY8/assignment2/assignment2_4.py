def facto(A):
    add=0
    for i in range(1,int(A/2)+1,1):
        if(A%i==0):
            print(i)
            add=int(add+i)

    print("Addition of that actorial=",add)

def main():
    print("enter the number=")
    no1=int(input())

    print("factorial of number=")
    facto(no1)


if __name__=="__main__":
    main()