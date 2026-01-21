#Write a program which accepts one number and prints sum of digits.

#Input: 123
#Output: 6

def SumDigits(No):
    Sum = 0

    while No != 0:
        Sum = Sum + (No % 10)
        No = No // 10

    print("Sum of digits:", Sum)

SumDigits(123)
