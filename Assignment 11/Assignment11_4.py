#Write a program which accepts one number and prints reverse of that number.

#Input: 123
#Output: 321

def Reverse(No):
    Rev = 0

    while No != 0:
        Rev = (Rev * 10) + (No % 10)
        No = No // 10
        
    print("Reverse number:", Rev)

Reverse(123)
