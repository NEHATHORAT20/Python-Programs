#Write a program which accept one number from user and return its factorial.
#Input : 5           Output : 120

def Factorial(No):
    Result = 1

    for i in range(1, No+1):
        Result = Result * i

    return Result

def main():
    No = 0
    No = int(input("Enter number : "))

    Ret = Factorial(No)
    print("Factorial is " , Ret)

if __name__ == "__main__":
    main()
