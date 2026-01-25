#Write a lambda function using map () which accepts a list of numbers and returns a list of squares of each number.

def main():
    Data = [1, 2, 3, 4, 5]
    print("The data is:", Data)

    Mdata = list(map(lambda No: No * No, Data))
    print("Square of numbers:", Mdata)

if __name__ == "__main__":
    main()

