import sys

#print(sys.getrecursionlimit())

#sys.setrecursionlimit(200)
#print(sys.getrecursionlimit())



def Display(No):
    Cnt=0
    if(No>0):
        print("Hello")
        No=No-1
        Display(No)    #recursive function call

Display(4)