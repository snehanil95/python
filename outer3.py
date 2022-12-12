

def Div(N1,N2):
    try:
        Ans=0
        Ans=N1/N2
        return Ans

    except ZeroDivisionError:
        print("Exception o division error occured")
