#Write a program which accepts one number and checks whether it is divisible by 3 and 5

#Input: 15
#Output: Divisible by 3 and 5

def Divisible(No):

    if(No % 3 == 0 and No % 5 == 0):
        print(No, "Divisible by 3 and 5")
    else:
        print(No, "Not divisible by 3 and 5")

Divisible(15)
