


def addition(arr,n):
    ans=0
    
    
    for i in range(0,n,1):
        ans=ans+arr[i]
    print(arr)
    return ans



def main():
    print("Enter how many  numbers you want to add:")
    no1=int(input())
    arr=[]
    print("enter the number you want to add:")

    for i in range(0,no1,1):
        al=int(input())
        arr.append(al)

    iRet=addition(arr,no1)

    print("Addition of given list is:",iRet)


if __name__ =="__main__":
    main()