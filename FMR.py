
def chkevn(no):
    return (no%2 ==0)

def doubles(no):
    return no*2

def sum(A,B):
    return A+B

def reduceX(helpFun,Data):
    ans=0
    for no in  Data:
        ans=helpFun(ans,no)

    return ans

def filterX(helpFun,Data):
    Rel=[]
    for no in Data:
        if(helpFun(no)==True):
            Rel.append(no)
    return Rel


def mapX(helpFun,Data):
    rel=[]
    for no in Data:
        Value=helpFun(no)
        rel.append(Value)

    return rel



def main():
    print("Enter number of elements you want to enter:")
    iSize=int(input())

    Data_Input=[]

    print("Please,enter the data:")

    for iCnt in range(0,iSize,1):
        Value=int(input())
        Data_Input.append(Value)

    print("Data is:",Data_Input)

    Data_filter=filterX(chkevn,Data_Input)

    print("Data after filter",Data_filter)

    Data_map=mapX(doubles,Data_filter)

    print("Data after map:",Data_map)

    output=reduceX(sum,Data_map)

    print("result after:",output)

if __name__ == "__main__":
    main()