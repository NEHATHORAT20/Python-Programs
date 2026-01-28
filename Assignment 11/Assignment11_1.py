#Write a program which accepts one number and checks whether it is prime or not.

#Input: 11
#Output: Prime Number

def Prime(No):

    if No <= 1:
        print("It is not a Prime Number")
        return
    
    for i in range(2, No):
        if No % i == 0:
            print("It is not a Prime Number")
            return
        
    print("It is a Prime Number")

Prime(11)
