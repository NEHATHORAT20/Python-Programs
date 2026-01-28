#Write a lambda function using filter () which accepts a list of numbers and returns a list of numbers divisible by both 3 and 5.

def main():
    Data = [10, 15, 30, 25, 45]
    print("The data is:", Data)

    Fdata = list(filter(lambda No: No % 3 == 0 and No % 5 == 0, Data))
    print("Numbers divisible by 3 and 5:", Fdata)

if __name__ == "__main__":
    main()
