#Write a program which accept N numbers from user and store it into List. 
#Return Minimum number from that List.
#Input : Number of elements : 4
#Input Elements : 13  5  45  7
#Output : 5

def Minimum(Data):
    
    Min = Data[0]
    
    for i in range(1, len(Data)):
        if Min > Data[i]:
            Min = Data[i]

    return Min

def main():
    Size = 0
    Value = 0
    Ret = 0

    Data = list()

    Size = int(input("Enter number of elements : "))

    for i in range(Size):
        Value = int(input())
        Data.append(Value)

    Ret = Minimum(Data)
    print("Minimum Element is :", Ret)

if __name__ == "__main__":
    main()