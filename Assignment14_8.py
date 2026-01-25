#Write a lambda function which accepts two numbers and returns addition.

def main():

    a = int(input("Enter first number : "))
    b = int(input("Enter second number : "))

    add = lambda a, b: a + b
    print("Addition is:", add(a, b))

if __name__ == "__main__":
    main()