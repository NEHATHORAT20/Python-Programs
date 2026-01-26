#Create on module named as Arithmetic which contains 4 functions as Add() for addition, Sub() for subtraction, Mult() for multiplication and Div() for division. 
#All functions accepts two parameters as number and perform the operation. 
#Write on python program which call all the functions from Arithmetic module by accepting the parameters from user.

import Arithmetic

def main():
    No1 = 0
    No2 = 0

    No1 = int(input("Enter first number : "))
    No2 = int(input("Enter second number : "))

    Addition = Arithmetic.Add(No1, No2)
    print("Addition is : " , Addition)

    Subtraction = Arithmetic.Sub(No1, No2)
    print("Substraction is : " , Subtraction)

    Multiplication = Arithmetic.Mult(No1, No2)
    print("Multiplication is : " , Multiplication)

    Division = Arithmetic.Div(No1, No2)
    print("Division is : " , Division)

if __name__ == "__main__":
    main()