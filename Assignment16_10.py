#Write a program which accept name from user and display length of its name.
#Input : Marvellous                Output : 10

def Length(Name):
    #return len(Name)
    Count = 0

    for ch in Name:
        Count = Count + 1
    return Count

def main():
    Name = input("Enter name : ")

    Ret = Length(Name)
    print(Ret)

if __name__ == "__main__":
    main()
