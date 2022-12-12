class BankAccount:
    ROI=10.5

    def __init__(self):
        self.Name=""
        self.Amount=00

    def Accept(self):
        print("Enter the name of account holder:")
        self.Name=input()

        print("Enter the initial  Amount:")
        self.Amount=int(input())

    def Display(self):
        print("Name of account holder:",self.Name)
        print("Amount:",self.Amount)

    def Diposite(self):
        print("Enter the ammount you want to deposite:")
        DAmount=int(input())
        self.Amount=self.Amount+DAmount

    def Withdraw(self):
        print("Enter the ammount you want to withdraw:")
        WAmount=int(input())
        self.Amount=self.Amount-WAmount

    def calculateROI(self):
        ROIAmount=(self.Amount*BankAccount.ROI)/100
        return ROIAmount

def main():
    obj=BankAccount()
    obj.Accept()
    ROIAmount=obj.calculateROI()
    print("--------------------------------------------")
    obj.Display()
    print("one year amount of interest on your account balance: ",ROIAmount)
    print("your amount after adding interest will be:",obj.Amount+ROIAmount)
   
   
    print("--------------------------------------------")
    obj.Diposite()
    print("After dipositing:")
    obj.Display()
    print("--------------------------------------------")
    obj.Withdraw()
    print("After withdraw:")
    obj.Display()
    print("--------------------------------------------")
    obj1=BankAccount()
    obj1.Accept()
    obj1.Display()
    ROIAmount=obj1.calculateROI()
    print("one year amount of interest on your account balance: ",ROIAmount)
    print("your amount after adding interest will be:",obj1.Amount+ROIAmount)
    print("--------------------------------------------")
    obj1.Diposite()
    print("After dipositing:")
    obj1.Display()
    print("--------------------------------------------")
    obj1.Withdraw()
    print("After withdraw:")
    obj1.Display()
    print("--------------------------------------------")

if __name__ =="__main__":
    main()