
def Add(A,B):
    return A+B

def Sub(A,B):
    return A-B

def Calculator(Target,N1,N2):
    return Target(N1,N2)




def Fun():
    print("Fun")


def Hello(FPTR):
    print("Hello")
    FPTR()

def Demo():
        print("Demo")

def main():
    #Hello()

    Hello(Demo)
    Hello(Fun)

    Ret=Calculator(Target=Add,N1=10,N2=11)
    print("Addition:",Ret)

    Ret=Calculator(Target=Sub,N1=10,N2=11)
    print("Substraction:",Ret)
    

if __name__ == "__main__":
    main()