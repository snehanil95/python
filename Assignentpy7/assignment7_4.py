import threading
def DisplaySmall(Arr):
    cnt=0
    print(threading.current_thread().name)
    print(id(threading.current_thread().name))
    for i in range(0,len(Arr)):
        if (Arr[i]>='a' and Arr[i]<= 'z'):
            print("Small character :",Arr[i])
            cnt=cnt+1
    print("Number of small characters:",cnt)   

def DisplayCapital(Arr):
    cnt=0
    print(threading.current_thread().name)
    print(id(threading.current_thread().name))
    for i in range(0,len(Arr)):
        if(Arr[i]>='A' and Arr[i]<='Z'):
            print("Capital character :",Arr[i])  
            cnt=cnt+1
    print("Number of capital characters:",cnt)    

def DisplayDigit(Arr):
    cnt=0
    print(threading.current_thread().name)
    print(id(threading.current_thread().name))
    for i in range(0,len(Arr)):
        if(Arr[i]>='0' and Arr[i]<='9'):
            print("Digits :",Arr[i])
            cnt=cnt+1
    print("Number of digits characters:",cnt)                     


print("Enter the string:")
List=input()


small=threading.Thread(target=DisplaySmall,args=(List,))
capital=threading.Thread(target=DisplayCapital,args=(List,))
Digit=threading.Thread(target=DisplayDigit,args=(List,))

print(threading.current_thread().name)
print(id(threading.current_thread().name))
small.start()
capital.start()
Digit.start()


small.join()


capital.join()
Digit.join()