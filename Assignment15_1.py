#Write a lambda function using map () which accepts a list of numbers and returns a list of squares of each number.

def Square(No):
    return No**2

def main():
    Data = [11,34,56,78]
    print("The data is: ", Data)

    Mdata = list(map(Square, Data))
    print("The data after mapping is: ", Mdata)

if __name__ == "__main__":
    main()
