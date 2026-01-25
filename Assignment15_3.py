#Write a lambda function using filter () which accepts a list of numbers and returns a list of odd numbers.

def main():
    Data = [1, 2, 3, 4, 5, 6]
    print("The data is:", Data)

    Fdata = list(filter(lambda No: No % 2 != 0, Data))
    print("Odd numbers are:", Fdata)

if __name__ == "__main__":
    main()
