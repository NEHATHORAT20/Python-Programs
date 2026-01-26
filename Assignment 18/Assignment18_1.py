#Write a program which accept N numbers from user and store it into List.
#Return addition of all elements from that List.
#Input : Number of elements : 6
#Input Elements : 13  5  45  7  4  56
#Output : 130

def ElementSum(Data):
    Sum = 0

    for i in range(len(Data)):
        Sum = Sum + Data[i]

    return Sum

def main():
    Size = 0
    Value = 0
    Ret = 0

    Data = list()

    Size = int(input("Enter the number of elements : "))

    for i in range(Size):
        Value = int(input("Input Element : "))
        Data.append(Value)

    Ret = ElementSum(Data)
    print("Addition of all elements : ", Ret)

if __name__ == "__main__":
    main()