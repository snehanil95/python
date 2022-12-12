class Numbers:
    def __init__(self):
        self.iValue=0

    def Accept(self):
        print("Enter the number:")
        self.iValue=int(input())

    def chkPrime(self):
        flag=False
        for i in range(2,int(self.iValue/2),1):
            if(self.iValue%i == 0):
                flag= False
            else:
                flag=True

        return flag

    def Factor(self):
        sum=0
        
        
        for i in range(2,self.iValue,1):
            if(self.iValue%i == 0):
                print(i)
                sum=sum+i
        return sum+1

    def sumFactor(self):
        sumF=self.Factor()
        print("Summation of Factors:",sumF)

    def chkperfect(self):
        sumF=self.Factor()
        if(sumF==self.iValue):
            flag=True

        else:
            flag=False

        return flag

def main():
    obj=Numbers()
    obj.Accept()
    print("---------------------------------------")

    BRet=obj.chkPrime()
    if(BRet==True):
        print("{} is not prime".format(obj.iValue))

    else:
        print("{} is  prime".format(obj.iValue))

    #obj.Factor()
    print("Factor of given value:",1)
    
    obj.sumFactor()

    rFlag=obj.chkperfect()
    if(rFlag==True):
        print("{} is perfect:".format(obj.iValue))

    else:
        print("{} is not perfect:".format(obj.iValue))

    print("---------------------------------------")
    obj1=Numbers()
    obj1.Accept()
    print("---------------------------------------")
    BRet=obj1.chkPrime()
    if(BRet==True):
        print("{} is not prime".format(obj1.iValue))

    else:
        print("{} is  prime".format(obj1.iValue))

    #obj.Factor()
    obj1.sumFactor()

    rFlag=obj1.chkperfect()
    if(rFlag==True):
        print("{} is perfect:".format(obj1.iValue))

    else:
        print("{} is not perfect:".format(obj1.iValue))
if __name__=="__main__":
    main()