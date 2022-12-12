#Due to miss reading

import threading
import sys
def sumEven(even,n1):
    sum=0
    for i in range(0,n1):
        sum=sum+even[i]
    
    print("Summation of even:",sum)

def sumOdd(odd,n2):
    sum=0
    for i in range(0,n1):
        sum=sum+odd[i]
    print("Summation of:",sum)

evenList=[]
oddList=[]

print("How many elements you want to add in even list:")
n1=int(input())

print("How many elements you want to add in odd list:")
n2=int(input())


print("Enter the numbers to add even list:")

for i in range(0,n1):
    
    no=int(input())
    if(no%2 ==0):
        evenList.append(no)
    else:
        print("Entered number is not Even,Re-enter the number:")
        sys.exit()


print("Enter the numbers to odd even list:")
for i in range(0,n1):
    no=int(input())
    if(no%2 !=0):
        oddList.append(no)
    else:
        print("Entered number is not Even,Re-enter the number:")
        sys.exit()


t1=threading.Thread(target=sumEven,args=(evenList,n1))
t2=threading.Thread(target=sumOdd,args=(oddList,n2))

t1.start()
t2.start()

t1.join()
t2.join()

print("Exit from main thread")