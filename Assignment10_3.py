#Write a program which accepts one number and prints factorial of that number.

#Input: 5
#Output: 120

def Factorial(No):
    Fact = 1

    for i in range(1, No + 1):
        Fact = Fact * i
        
    print("Factorial is:", Fact)

Factorial(5)
