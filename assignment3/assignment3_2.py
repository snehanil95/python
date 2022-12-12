


def maxnum(arr,n):
    maxn=0
    
    
    for i in range(0,n,1):
        if(arr[i]>maxn):
            maxn=arr[i]
    print(arr)
    return maxn



def main():
    print("Enter how many  numbers you want to add in list:")
    no1=int(input())
    arr=[]
    print("enter the numbers in list:")

    for i in range(0,no1,1):
        Data_Input=int(input())
        arr.append(Data_Input)

    iRet=maxnum(arr,no1)

    print("Maximum number:",iRet)


if __name__ =="__main__":
    main()