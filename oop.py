
class Ariht:
    def __init__(self,A,B):
        self.no1=A
        self.no2=B


    def add(self):
        return self.no1+self.no2

    def sub(self):
        return self.no1-self.no2



def main():
    print("enter first number:")
    no1=int(input())

    print("enter first number:")
    no2=int(input())

    
    obj=Ariht(no1,no2)

    ret=obj.add()
    print("Addition is",ret)

    ret=obj.sub()
    print("Substraction is",ret)

if __name__ =="__main__":
    main()