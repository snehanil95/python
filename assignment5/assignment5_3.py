class Arithmatic:
    def __init__(self):
        self.value1=0
        self.value2=0

    def Accept(self):
        print("Enter the first number:")
        self.value1=int(input())

        print("Enter the second number:")
        self.value2=int(input())
    
    def Addition(self):
       return self.value1 + self.value2

    def substraction(self):
        return self.value1 - self.value2

    def Multiplication(self):
        return self.value1 * self.value2

    def Division(self):
        return self.value1 / self.value2

   
def main():

    obj=Arithmatic()

    obj.Accept()
    print("Adddition:",obj.Addition())
    print("substraction",obj.substraction())
    print("Multiplication:",obj.Multiplication())
    print("Division:",obj.Division())

if __name__ =="__main__":
    main()