#iput:4
#output:4 3 2 1


def Display(no):
    if(no!=0):
        print(no,end=" ")
        no=no-1
        Display(no)


print("Enter the number from user:")
no=int(input())
Display(no)