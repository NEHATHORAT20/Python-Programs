#Write a program which contains one function that accept one number from user and returns true if number is divisible by 5 otherwise return false.
#Input : 8               Output : False
#Input : 25              Output : True

def Divisible(No):
    if No % 5 == 0:
        return True
    else: 
        return False
    
def main():
    No = 0
    No = int(input("Enter number : "))

    Ret = Divisible(No)
    print(Ret)

if __name__ == "__main__":
    main()
