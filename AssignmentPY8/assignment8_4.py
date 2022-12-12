Digit=0
sum=0
def SumDigit(no):
    global Digit
    global sum
    if(no!=0):
       Digit=no%10
       no=no/10
       sum=sum+Digit
       SumDigit(no)
    return sum    
        
        


print("Enter the number from user:")
no=int(input())
Ret=SumDigit(no)
print("Sumation of digit:",Ret)