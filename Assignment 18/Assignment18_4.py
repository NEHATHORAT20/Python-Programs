#Write a program which accept N numbers from user and store it into List.
#Accept one another number from user and return frequency of that number from List.
#Input : Number of elements : 11
#Input Elements : 13  5  45  7  4  56  5  34  2  5  65
#Element to search : 5
#Output : 3

def FrequencyCount(Data, No):
    Count = 0

    for i in range(len(Data)):
        if Data[i] == No:
            Count = Count + 1

    return Count

def main():
    Size = 0
    Value = 0
    Ret = 0

    Data = list()

    Size = int(input("Enter the number of elements : "))

    for i in range(Size):
        Value = int(input())
        Data.append(Value)

    print("Enter number which you want to search in list : ")
    No = int(input())

    Ret = FrequencyCount(Data, No)
    print("Frequency Count of Number is : ", Ret)

if __name__ == "__main__":
    main()