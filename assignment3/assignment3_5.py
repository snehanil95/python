

def chkprime(num):
    iCnt=0

    for i in range(2,num-1,1):
        
        if(num%i==0):
            iCnt=iCnt+1
        
                
    #print("***",iCnt)


    if(iCnt>0):
        return False
    else:
        return True

def Listprime(arr,n):
    ls=[]
    print("in def",arr )
    for no in arr:
        if(chkprime(no)==True):
            print(no)
            ls.append(no)
            
        
    print(ls)    
    return ls

def addl(arr):
    add=0
    for i in range(0,len(arr),1):
        add=add+arr[i]

    return add

def main():
    print("Enter how many  numbers you want to add in list:")
    no1=int(input())
    arr=[]
    print("enter the numbers in list:")

    for i in range(0,no1,1):
        Data_Input=int(input())
        arr.append(Data_Input)
    
    
    iRetlist=[]
    iRetlist=Listprime(arr,no1)

    print("prime numbers:",iRetlist)

    IRet=addl(iRetlist)
    print("Addition of prime number:",IRet)
if __name__ =="__main__":
    main()
