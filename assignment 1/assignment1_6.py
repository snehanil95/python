#check number positive,nigative or zero
def main():
    print("enter a number=")
    no=int(input())

    if(no == 0):
        print("number is zero")

    if(no <0):
        print("number is negative")

    if(no>0):
        print("number is positive")



if __name__ =='__main__':
    main()