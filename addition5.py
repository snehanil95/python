print("demostration of industrial program")
import mod
print("value of main",__name__)
def main():

    print("enter first number:")
    no1=int(input())
    #print(type(no1))
    print("enter sencond number:")
    no2=int(input())
    ans=mod.addition(no1,no2)
    print("Addition is:",ans)

if __name__=="__main__":
    main()