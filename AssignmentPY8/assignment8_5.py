def fact(no):
    if(no==0):
        return 1

    return no*fact(no-1)

print("Enter the number:")
no=int(input())
Ret=fact(no)
print("Factorial of {}:",format(no),Ret)