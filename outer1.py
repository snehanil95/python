def Substraction(N1,N2):
    Ans=0
    Ans=N1-N2
    return Ans


def Decorated_Fun(Fun_Name):
    def Inner(A,B):
        if(A<B):
            A,B=B,A

        return Fun_Name(A,B)
    return Inner

v1=int(input("Enter first numeber:"))
v2=int(input("Enter second numeber:"))

New_Fun=Decorated_Fun(Substraction)
print(New_Fun(v1,v2))