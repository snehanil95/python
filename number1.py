class numbers:
    def __init__(self):
        self.Size=0
        self.arr=list()
        self.Accept()

    def Accept(self):
        print("How many element you want to store?")
        self.Size=int(input())

        print("Please,Enter the element:")
        value=0
        for i in range(0,self.Size):
            value=int(input())
            self.arr.append(value)

    def Summation(self):
        sum=0
        for i in range(0,self.Size):
            sum=sum+self.arr[i]
        return sum

    def Average(self):
        sum=0
        for i in range(0,self.Size):
            sum=sum+self.arr[i]
        return (sum/self.Size)


    def maximum(self):
        max=self.arr[0]

        for i in range(0,self.Size):
            if(self.arr[i]>max):
                max=self.arr[i]

        return max


    def minimum(self):
        min=self.arr[0]

        for i in range(0,self.Size):
            if(self.arr[i]<min):
                min=self.arr[i]

        return min

    def Display(self):
        print("Elements from lisst are:")
        for i in range(0,self.Size):
            print(self.arr[i])


def main():
    
    

    obj=numbers()
    #obj.Accept()
    obj.Display()
    output=obj.Summation()

    print("Summation of all element is:",output)

    Ret=obj.Average()
    print("Average:",Ret)

    Ret1=obj.maximum()
    print("largest element:",Ret1)

    Ret2=obj.minimum()
    print("minimum:",Ret2)

if __name__ == "__main__":
    main()