import time
from multiprocessing import Process

import os


def DisEven(No):
    print("Even number:")
    for i in range(2,No,2):
        print(i)


def DisOdd(No):
    print("Odd numbers:")
    for i in range(1,No,2):
        print(i)


def main():
    print("Demostration os parallel programming multi processes:")
    Num=2000

    p1 = multiprocessing.Process(target = DisEven,args = (Num,))
    p2 = multiprocessing.Process(target = DisOdd,args = (Num,))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    print("End of main:")

if __name__=="__main__":
    start_time=time.process_time()
    main()
    end_time=time.process_time()
    print("Execution time:",end_time-start_time)