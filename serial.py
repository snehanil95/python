def square(no):
    return no*no


def main():
    Data=[1,2,3,4]

    result=[]

    for val in Data:
        result.append(square(val))

    print(result)


if __name__ =="__main__":
    main()