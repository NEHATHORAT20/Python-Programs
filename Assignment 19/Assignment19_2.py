#Write a program which contains one lambda function which accepts two parameters and return its multiplication.
#Input : 4  3           Output : 12
#Input : 6  3           Output : 18

Multiplication = lambda A, B : A * B

def main():
    No1 = int(input("Enter first number : "))
    No2 = int(input("Enter second number : "))

    Ret = Multiplication(No1, No2)
    print("Multiplication is : ", Ret)

if __name__ == "__main__":
    main()