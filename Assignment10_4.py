#Write a program which accepts one number and prints all even numbers till that number.

#Input: 10
#Output: 2 4 6 8 10

def Even(No):
    for i in range(1, No+1):
        if i % 2 == 0:
            print(i)

Even(10)