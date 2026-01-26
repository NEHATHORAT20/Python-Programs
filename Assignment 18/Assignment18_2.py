#Write a program which accept N numbers from user and store it into List. 
#Return Maximum number from that List.
#Input : Number of elements : 7
#Input Elements : 13  5  45  7  4  56  34
#Output : 56

def Maximum(Data):
    Max = Data[0]
    
    for i in range(1, len(Data)):
        if Max < Data[i]:
            Max = Data[i]
            
    return Max

def main():
    Size = 0
    Value = 0
    Ret = 0

    Data = list()

    Size = int(input("Enter the number of elements : "))

    for i in range(Size):
        Value = int(input())
        Data.append(Value)

    Ret = Maximum(Data)
    print("Maximum element in list is : ", Ret)
    
if __name__ == "__main__":
    main()