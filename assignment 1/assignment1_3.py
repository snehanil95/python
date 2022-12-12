#addition of two numbers
def addnum(A,B):
    sum=A+B
    return sum
def main():
    print("enter the first number=")
    no1 = int(input())
    print("enter the second number=")
    no2 = int(input())

    ret=addnum(no1,no2)
    print("Addition of two numbers=",ret)
if __name__=='__main__':
    main()