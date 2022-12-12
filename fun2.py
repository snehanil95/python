print("positional arguments")

def Add(no1,no2):
    print("value of no1",no1)
    print("value of no1",no2)
    return no1+no2


def sub(no1,no2):
    print("value of no1",no1)
    print("value of no1",no2)
    return no1-no2

def main():
    ans=0
    ans=Add(10,12)
    print("Additon is",ans)

    print("keyword argument")
    ans=sub(no2=10,no1=12)
    print("substraction is",ans)

if __name__=="__main__":
    main()file:///home/snehanil/2python/parameter.py
