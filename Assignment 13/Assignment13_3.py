#Write a program which accepts one number and checks whether it is perfect number or not.

#Input: 6
#Output: Perfect Number

def Perfect(No):
    Sum = 0

    for i in range(1, No):
        if No % i == 0:
            Sum = Sum + i
            
    if Sum == No:
        print("Perfect Number")
    else:
        print("Not perfect Number")

Perfect(6)
