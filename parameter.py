
def Area(Radius,PI):
    Result=PI*Radius*Radius
    return Result

def main():
    RValue=10.5
    PI=3.14

    Ans=Area(RValue,PI)
    print("Area of circle",Ans)

    Ans=Area(PI=PI,Radius=RValue)
    print("Area of circle",Ans)


if __name__ == "__main__":
    main()