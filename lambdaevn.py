def checkEvn(no):
    if(no%2  == 0):
        return True
    else:
        return False

def checkEvnX(no):
        return(no%2 ==0)       
even=lambda no : no%2 ==0
Ret=even(12)

if(Ret == True):
    print("even")
else:
    print("odd")

