def add(*values):
    print(type(values))
    print("length",len(values))

    sum =0
    for no in values:
        sum = sum+no


    return sum

def addX(*values1):
    sum1=0
    print(len(values1))
    no=0
    for no in range(0,len(values1),1):
        sum1=sum1+no

    return sum1
def main():
    Ans=0
    Ans=add(10,11,32,45,6,5)
    print("Additon is",Ans)
    Ans1=0
    Ans1=addX(10,11,32,45,6)
    print("Additon is",Ans1)


if __name__ == "__main__":
    main()