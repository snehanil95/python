from functools import reduce



    








def main():
    print("Enter number of elements you want to enter:")
    iSize=int(input())

    Data_Input=[]

    print("Please,enter the data:")

    for iCnt in range(0,iSize,1):
        Value=int(input())
        Data_Input.append(Value)

    print("Data is:",Data_Input)

    Data_filter=
    
    print("Data after filter",Data_filter)

    Data_map=
    


    print("Data after map:",Data_map)

    output=int(reduce(lambda A,B:A+B,list(map(lambda no:no*2,list(filter(lambda no :(no%2 ==0),Data_Input))))

    print("result after:",output)

if __name__ == "__main__":
    main()