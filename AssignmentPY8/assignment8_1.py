def Display(no):
    if(no!=0):
        print("*",end=" ")
        no=no-1
        Display(no)


print("Enter the number from user:")
no=int(input())
Display(no)