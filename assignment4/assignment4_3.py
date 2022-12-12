from functools import reduce

incease=lambda no:(no>=70 and no<=90)
IncByTen=lambda no:(no+10)
mult=lambda no1,no2:(no1*no2)
def main():
    print("How many numbers you want to add in list:")
    no=int(input())
    Data_input=[]
    
    print("Enter the number in list:")
    for i in range(0,no,1):
        Value=int(input())
        Data_input.append(Value)

    Out_List1=list(filter(incease,Data_input))
    print("output from filter number is greater than 70:",Out_List1)

    Out_List2=list(map(IncByTen,Out_List1))
    print("output from map filtered output increase by 10",Out_List2)

    Out_List3=int(reduce(mult,Out_List2))
    print("output from reduce product of map:",Out_List3)


if __name__ =="__main__":
    main() 