#Write a program which accept number from user and return addition of digits in that number.
#Input : 5187934            Output : 37

def DigitSum(No):
    Sum = 0

    while(No > 0):
        Digit = No % 10
        Sum = Sum + Digit
        No = No // 10
    
    return Sum

def main():
    No = 0
    No = int(input("Enter Number : "))

    Ret = DigitSum(No)
    print("Addition of digits : " , Ret)

if __name__ == "__main__":
    main()