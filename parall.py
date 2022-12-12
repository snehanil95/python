import os
import multiprocessing

def square(no):
    print("pid of worker is {} for input {}".format(os.getpid(),no))
    return no*no


def main():
    print("process pidof our application",os.getpid())
    Data=[1,2,3,4,5]

    result=[]

    pobj =multiprocessing.Pool()

    result=pobj.map(square,Data)
    print(result)


if __name__ =="__main__":
    main()