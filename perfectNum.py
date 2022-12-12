class Num:
    def __init__(self):
        self.N=0
        self.arr=[]

    def Accept(self):
        value=0
        print("Enter how many element you want to add:")
        self.N=int(input())

        print("Enter the number to insert in list:")
        for i in range(0,self.N):
            value=int(input())
            self.arr.append(value)

    def Display(self):
        print("Element of list:")
        for i in range(0,self.N):
            print(self.arr[i])

    def primeChk(self,No):

        for i in range(2,self.N):

            if(No%i==0):
                return True

            else:
                return false
    
    
    def chk(self):
        for i in range(0,self.N):
            flag=self.primeChk(self.arr[i])
        
        
        if(flag==True):
            print("{} Number is not prime".format(self.arr[i]))

        else:
            print("{} Number is prime".format(self.arr[i]))



def main():
    obj=Num()
    obj.Accept()
    obj.Display()
    obj.chk()
    
    


if __name__ == "__main__":
    main()