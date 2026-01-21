#Write a program which accepts one number and prints its factors.

#Input: 12
#Output: 1 2 3 4 6 12

def Factors(No):
    for i in range(1, No+1):
        if No % i == 0:
            print(i)

Factors(12)