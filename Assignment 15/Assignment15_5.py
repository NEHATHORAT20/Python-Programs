#Write a lambda function using reduce () which accepts a list of numbers and returns the maximum element.

from functools import reduce

def main():
    Data = [10, 5, 20, 8]
    print("The data is:", Data)

    Max = reduce(lambda A, B: A if A > B else B, Data)
    print("Maximum number is:", Max)

if __name__ == "__main__":
    main()
)
