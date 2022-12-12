def Outer():
    print("Outer")

    def Inner():
        print("Inner")
    print(id(Inner))
    return Inner


ret=Outer()
print(type(ret))
print(id(ret))
ret()