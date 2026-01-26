#Write a program which accepts one number and prints sum of first N natural numbers.

#Input: 5
#Output: 15

def SumNatural(No):
    Sum = 0

    for i in range(1, No+1):
        Sum = Sum + i
    print("Sum is : " , Sum)

SumNatural(5)
