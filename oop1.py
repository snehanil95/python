class Arithmatic:
    def __init__(self,A,B):
        print("Inside init method")
        self.No1=A
        self.No2=B

    def Add(self):
        Ans=self.No1+self.No2
        return Ans


    def Sub(self):
        Ans=self.No1-self.No2
        return Ans



def main():
    print("Inside main method")

    obj=Arithmatic(11,10)
    output=obj.Add()
    print("Addition is:",output)

    output=obj.Sub()
    print("Addition is:",output)


if __name__ == "__main__":
    print("Inside Stater")
    main()