#Write a program which accepts one number and checks whether it is palindrome or not.

#Input: 121
#Output: Palindrome

def CheckPalindrome(No):
    Temp = No
    Rev = 0

    while No != 0:
        Rev = (Rev * 10) + (No % 10)
        No = No // 10

    if Temp == Rev:
        print("Palindrome")
    else:
        print("Not Palindrome")

CheckPalindrome(121)