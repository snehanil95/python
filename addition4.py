print("demostration of industrial program")
def addition(v1,v2):
    a=v1+v2
    return a

def main():
    print("enter first number:")
    no1=int(input())
    #print(type(no1))
    print("enter sencond number:")
    no2=int(input())
    ans=addition(no1,no2)
    print("Addition is:",ans)

if __name__=="__main__":
    main()