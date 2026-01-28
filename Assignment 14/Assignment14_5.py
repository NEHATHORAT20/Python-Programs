#Write a lambda function which accepts one number and returns True if number is even otherwise False.

CheckEven = lambda No : (No % 2 == 0)

def main():
    Value = 0
    Ret = False
    
    print("Enter number : ")
    Value = int(input())
    Ret = CheckEven(Value)

    if(Ret == True):
        print("True")
    else:
        print("False")
    
if __name__ == "__main__":
    main() 
