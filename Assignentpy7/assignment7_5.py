import threading
import time

def DisplayNum():
    for i in range(1,50):
        print(i)
def DisplayRev():
    time.sleep(2)
    for i in range(50,1,-1):
        print(i)


thread1=threading.Thread(target=DisplayNum)
thread2=threading.Thread(target=DisplayRev)

thread1.start()
thread1.join()

thread2.start()
thread2.join()