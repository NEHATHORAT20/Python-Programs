#Write a program which accept number from user and return number of digits in that number
#Input : 5187934            Output : 7

def DigitCount(No):
    count = 0

    while(No > 0):
        count = count + 1
        No = No // 10
    
    return count


def main():
    No = 0
    No = int(input("Enter Number : "))

    Ret = DigitCount(No)
    print("Digit Count is : " , Ret)

if __name__ == "__main__":
    main()
