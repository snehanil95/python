def main():
    try:
        print("Enter the first num:")
        No1=int(input())

        print("Enter the second num:")
        No2=int(input())

    
        Ans=No1/No2
        print("Div:",Ans)

    except ZeroDivisionError:
        print("Exception 0error occured")

    except ValueError:
        print("Exception value occured")



    finally:
        print("Inside finally block")


if __name__ == "__main__":
    main()