
print("1.function which accept nothing and return nothing")
def Demo():
    print("Iside demo ")

def Demo2(no):
    print("2.function which accept number and return nothing")
    print("inside Demo2 with argument=",no)

def Demo3(no):
    print("3.function which accept and return ")
    return no+2

def Demo4(no1,no2):
    print("4.function which accept 2 numbers and return 1 number")
    print("inside demo4")
    add=no1+no2
    return add

def Demo5(no1,no2):
    print("5.function which accept 2 parameters and return 2 ")
    print("inside demo5")
    add=no1+no2
    sub=no1-no2
    return add,sub

def main():
    Demo()
    Demo2(10)
    ans=Demo3(10)
    print("return value of Demo3",ans)
    ans=Demo4(10,11)
    print("Addition is=",ans)
    ans1,ans2=Demo5(11,20)
    print("first return value:",ans1)
    print("second return value:",ans2)

if __name__=="__main__":
    main()