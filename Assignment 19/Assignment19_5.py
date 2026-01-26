#Write a program which contains filter(), map() and reduce() in it. 
#Python application which contains one list of numbers. 
#List contains the numbers which are accepted from user. 
#Filter should filter out all prime numbers. 
#Map function will multiply each number by 2. 
#Reduce will return Maximum number from that numbers. 
#(You can also use normal functions instead of lambda functions).
#Input List = [2, 70, 11, 10, 17, 23, 31, 77]
#List after filter = [2, 11, 17, 23, 31]
#List after map = [4, 22, 34, 46, 62]
#Output of reduce = 62

from functools import reduce

def ChkPrime(No):
    for i in range(2, No):
        if No % i == 0:
            return False
    return True

def Multiply(No):
    return 2 * No

def Maximum(No1, No2):
    if No1 > No2:
        return No1
    else:
        return No2

def main():
    Size = 0
    Value = 0

    Data = list()

    Size = int(input("Enter size of list : "))

    for i in range(Size):
        Value = int(input())
        Data.append(Value)

    FData = list(filter(ChkPrime, Data))
    print("List after filter : ", FData)

    MData = list(map(Multiply, FData))
    print("List after map :", MData)

    RData = reduce(Maximum, MData)
    print("Output of reduce :", RData)

if __name__ == "__main__":
    main()