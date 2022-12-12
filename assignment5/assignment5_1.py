class Demo:
    value=12
    def __init__(self,A,B):
        self.no1=A
        self.no2=B


    def fun(self):
        print("value of no1 in fun:",self.no1)
        print("value of no2 in fun:",self.no2)
        print("value of instance variable in fun:",int(Demo.value))


    def gun(self):
        print("value of no1 in gun:",self.no1)
        print("value of no2 in gun:",self.no2)
        print("value of instance variable in gun:",int(Demo.value))



def main():
    print("enter first number:")
    no1=int(input())

    print("enter first number:")
    no2=int(input())

    
    obj=Demo(no1,no2)
    obj.fun()
    obj.gun()

    obj1=Demo(11,21)
    obj1.fun()
    obj1.gun()

    obj2=Demo(51,101)
    obj2.fun()
    obj2.gun()



if __name__ == "__main__":
    main()