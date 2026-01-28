#Write a program which accepts one number and prints that many numbers in reverse order.

#Input: 5
#Output: 5 4 3 2 1

def Reverse(No):
    for i in range(No, 0, -1):
        print(i)

Reverse(5)
