class value:

    def __init__(self,data):
            self.No=data


    def sumFactor(self):
        sum=0

        for i in range(0,self.No):
                if(self.No%i ==0):
                    sum=sum+i

        return sum

    def Checkperfect(self):
        Ans=self.sumFactor()

        if(Ans==self.No):
            return True
        else:
            return False



def main():
        print("Enter the number:")
        N=int(input())

        obj=value(N)

        Ret=obj.Checkperfect()

        if(Ret==True):
            print("{} is a perfect number:".format(A))

        else:
            print("{} is a perfect number:".format(A))




if __name__ == "__main__":
        main()
