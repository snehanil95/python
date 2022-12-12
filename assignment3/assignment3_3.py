


def minnum(arr,n):
    
    for i in range(0,n,1):
        minn=arr[i]
        if(minn>arr[i]):
            minn=arr[i]
    print(arr)
    return minn



def main():
    print("Enter how many  numbers you want to add in list:")
    no1=int(input())
    arr=[]
    print("enter the numbers in list:")

    for i in range(0,no1,1):
        Data_Input=int(input())
        arr.append(Data_Input)

    iRet=minnum(arr,no1)

    print("Minimum number:",iRet)


if __name__ =="__main__":
    main()