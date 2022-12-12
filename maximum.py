print("to find out maximum number")

def maximum(no1,no2):
    if no1>no2:
        return no2
    else :
        return no2

def main():
    print("enter first number:")
    value1=input()

    print("enter second number:")
    value2=input()

    ans=maximum(int(value1),int(value2))

    print("largest number is:",ans)

if __name__=="__main__":
    main()