def main():
    print("Enter the first number:")
    no1=int(input())

    print("Enter the second number:")
    no2=int(input())

    mult=lambda no1,no2: no1*no2
    print("Multiplication is:",mult(no1,no2))


if __name__ == "__main__":
    main()