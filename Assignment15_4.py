#Write a lambda function using reduce () which accepts a list of numbers and returns the addition of all elements.

from functools import reduce

def main():
    Data = [1, 2, 3, 4, 5]
    print("The data is:", Data)

    Rdata = reduce(lambda A, B: A + B, Data)
    print("Addition is:", Rdata)

if __name__ == "__main__":
    main()
