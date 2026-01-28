#Write a lambda function which accepts three numbers and returns largest number.

def main():

    a = int(input("Enter first number : "))
    b = int(input("Enter second number : "))
    c = int(input("Enter third number : "))

    Largest = lambda a, b, c: max(a,b,c)
    print("Largest number is :", Largest(a, b, c))

if __name__ == "__main__":
    main()
