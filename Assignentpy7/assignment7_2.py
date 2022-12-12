import threading


def evenFactor(No):
    sum=0
    for i in range(2,int(No/2)+1,2):
        if(No%i == 0):
            print("Even factor:",i)
            sum=sum+i
    print("Summation of even factor:",sum)


def oddFactor(No):
    sum=0
    for i in range(1,int(No/2)+1,2):
        if(No%i == 0):
            print("Odd factors:",i)
            sum=sum+i
    print("Summation of odd factors:",sum)




print("Enter the number:")
Num=int(input())    

t1=threading.Thread(target=evenFactor,args=(Num,))
t2=threading.Thread(target=oddFactor,args=(Num,))

t1.start()
t2.start()

t1.join()
t2.join()

print("Exit from main")