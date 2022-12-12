class Circle:
    PI=3.14
    def __init__(self):
        self.Radius=0
        self.circumference=0
        self.area=0


    def Accept(self):
        print("enter Radius:")
        self.Radius=int(input())

    def CalArea(self):
        self.area=(Circle.PI)*(self.Radius)*(self.Radius)

    def CalCircumference(self):
        self.circumference=2*Circle.PI*self.Radius
        
    def Display(self):
        print("Radius=",self.Radius)
        print("Area:",self.area)
        print("circumference:",self.circumference)

def main():

    obj=Circle()

    obj.Accept()
    obj.CalArea()
    obj.CalCircumference()
    obj.Display() 


   



if __name__ == "__main__":
    main()