from functools import reduce

Even=lambda no:(no%2 == 0)
square=lambda no:(no*no)
add=lambda no1,no2:(no1+no2)
def main():
    print("How many numbers you want to add in list:")
    no=int(input())
    Data_input=[]
    
    print("Enter the number in list:")
    for i in range(0,no,1):
        Value=int(input())
        Data_input.append(Value)

    Out_List1=list(filter(Even,Data_input))
    print("output from filter number is even:",Out_List1)

    Out_List2=list(map(square,Out_List1))
    print("output from map square of that even number",Out_List2)

    Out_List3=int(reduce(add,Out_List2))
    print("output from reduce addition of map:",Out_List3)


if __name__ =="__main__":
    main() 