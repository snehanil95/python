


def frqnum(arr,n1,n2):
    
    
    iCnt=0
    for i in range(0,n1,1):
        if(n2==arr[i]):
            iCnt=iCnt+1
    print(arr)
    return iCnt



def main():
    print("Enter how many  numbers you want to add in list:")
    no1=int(input())
    arr=[]
    print("enter the numbers in list:")

    for i in range(0,no1,1):
        Data_Input=int(input())
        arr.append(Data_Input)
    print("enter the element to search:")
    no2=int(input())
    iRet=frqnum(arr,no1,no2)

    print("frequency number:",iRet)


if __name__ =="__main__":
    main()