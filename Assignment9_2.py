#Write a program which contains one function ChkGreater () that accepts two numbers and prints the greater number.

#Input: 10 20
#Output: 20 is greater

def ChkGreater():
    No1 = 10
    No2 = 20

    if (No1 > No2):     
        print("10 is greater")
    else:
        print("20 is greater")

ChkGreater()

print("------------------------------------------------")

def ChkGreater(No1, No2):
    
    if No1 > No2:
        print(No1, "is greater")
    else:
        print(No2, "is greater")

ChkGreater(10, 20)