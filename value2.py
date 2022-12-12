class value:
    def __init__(self,data):
            self.No=data


    def sumFactor(self):
        sum=0

        for i in range(0,self.No):
                if(self.No%i ==0):
                    sum=sum+i

        return sum




    def prime(self):
        ret=self.sumFactor()

        if(ret==1):
            return True


def main():
    print("Enter the number:")
    n=int(input())

    obj=value(n)

    p=obj.prime()

    if(p==True):
        print("not prime")


if __name__ == "__main__":
    main()