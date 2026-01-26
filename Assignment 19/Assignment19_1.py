#Write a program which contains one lambda function which accepts one parameter and return power of two.
#Input : 4              Output : 16
#Input : 6              Output : 64

Power = lambda No : 2 ** No

def main():
    No = int(input("Enter number : "))

    Ret = Power(No)
    print("Power of 2 is : ", Ret)

if __name__ == "__main__":
    main()