#Write a lambda function which accepts one number and returns True if divisible by 5.

def main():

    No = int(input("Enter number : "))

    Div = lambda a : a % 5 == 0
    print("Divisible by 5 :", Div(No))

if __name__ == "__main__":
    main()
