#Write a lambda function using filter () which accepts a list of numbers and returns the count of even numbers.

def main():
    Data = [11, 34, 56, 78]
    print("The data is:", Data)

    Fdata = list(filter(lambda No: No % 2 == 0, Data))
    print("Count of even numbers is:", len(Fdata))

if __name__ == "__main__":
    main()
