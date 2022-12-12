import threading

def DisplayEven(No):
    
    
    for i in range(1,No,1):
        #print("even number:")
        if(i%2 == 0):
            print("Even:",i)

def DisplayOdd(No):
    
    
    for i in range(1,No,1):
        #print("Odd number:")
        if(i%2 != 0):
            print("Odd;",i)

num=20


t1=threading.Thread(target=DisplayEven,args=(num,))
t2=threading.Thread(target=DisplayOdd,args=(num,))


t1.start()
t2.start()

t1.join()
t2.join()