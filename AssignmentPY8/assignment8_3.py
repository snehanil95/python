#input:5
#output:1 2 3 4 5

i=1
def Display(no):
    global i
    if(no!=0):
        
        
        print(i,end=" ")
        i=i+1

        no=no-1
        Display(no)


print("Enter the number from user:")
no=int(input())
Display(no)