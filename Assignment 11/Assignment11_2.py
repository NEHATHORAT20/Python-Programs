#Write a program which accepts one number and prints count of digits in that number.

#Input: 7521
#Output: 4

def CountDigits(No):
    
    Cnt = 0

    while No != 0:
        Cnt = Cnt + 1
        No = No // 10   #removes last digit of number
    
    print("Count of digits:", Cnt)

CountDigits(7521)
