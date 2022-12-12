def main():
    print("Enter the number:")
    no=int(input())

    square=lambda no: no*no
    print("power of two :",square(no))


if __name__ == "__main__":
    main()