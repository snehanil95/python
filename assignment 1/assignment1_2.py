def ChkNum(A):


    if(A%2 == 0):
        print("number is Even")
    else:
        print("number is odd")


def main():
    print("enter the number:")
    no=int(input())

    ChkNum(no)

if __name__ =='__main__':
    main()