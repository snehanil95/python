import time
import multiprocessing


def DisEven(No):
    print("Even number:")
    for i in range(2,No,2):
        print(i)


def DisOdd(No):
    print("Odd numbers:")
    for i in range(1,No,2):
        print(i)


def main():
    print("Demostration os serial programming:")
    DisEven(2000)
    DisOdd(2000)


if __name__=="__main__":
    start_time=time.process_time()
    main()
    end_time=time.process_time()
    print("Execution time:",end_time-start_time)