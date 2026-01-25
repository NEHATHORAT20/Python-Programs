#Write a lambda function using filter () which accepts a list of strings and returns a list of strings having length greater than 5.

def main():
    Data = ["Python", "Java", "Angular", "C"]
    print("The data is:", Data)

    Fdata = list(filter(lambda Str: len(Str) > 5, Data))
    print("Strings with length > 5:", Fdata)

if __name__ == "__main__":
    main()
