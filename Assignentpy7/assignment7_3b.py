import threading
import sys
def sumEven(even,n1):
    sum=0
    for i in range(0,n1):
        if(even[i]%2==0):
            sum=sum+even[i]
    
    print("Summation of even:",sum)

def sumOdd(odd,n2):
    sum=0
    for i in range(0,n1):
        if(odd[i]%2!=0):
            sum=sum+odd[i]
    print("Summation of odd:",sum)

List=[]

print("How many elements you want to add in  list:")
n1=int(input())

print("Enter the numbers to add even list:")

for i in range(0,n1):
    no=int(input())
    List.append(no)


evenList=threading.Thread(target=sumEven,args=(List,n1))
oddList=threading.Thread(target=sumOdd,args=(List,n1))

evenList.start()
oddList.start()

evenList.join()
oddList.join()