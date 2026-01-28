#Write a lambda function using reduce () which accepts a list of numbers and returns the minimum element.

from functools import reduce

def main():
    Data = [11, 34, 56, 78]
    print("The data is:", Data)

    Min = reduce(lambda A, B: A if A < B else B, Data)
    print("Minimum number is:", Min)

if __name__ == "__main__":
    main()
)
