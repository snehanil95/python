
def main():
    arr=list()
    print("enter how many number in list")
    n=int(input())

    print("enter the numbers=")
    for i in range(0,n):
        no=int(input())
        arr.append(no)
    print(arr)
if __name__ == "__main__":
     main()