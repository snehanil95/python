import functools from reduce
def chkprime(no):
    iCnt=0
    for i in range(2,int(no/2)+1,1):
        if(no%i ==0):
            iCnt=iCnt+1
            
    if(iCnt>1):    
        return True
    else :
            return False
    
            


def doubles(no):
    return no*2

def max(A,B):
     if(A<B):
        return B





def main():
    print("Enter number of elements you want to enter:")
    iSize=int(input())

    Data_Input=[]

    print("Please,enter the data:")

    for iCnt in range(0,iSize,1):
        Value=int(input())
        Data_Input.append(Value)

    print("Data is:",Data_Input)

    Data_filter=list(filter(chkprime,Data_Input))

    print("Data after filter",Data_filter)

    Data_map=map(doubles,Data_filter)

    print("Data after map:",Data_map)

    output=reduce(max,Data_map)

    print("result after:",output)

if __name__ == "__main__":
    main()
