#Write a lambda function which accepts two numbers and returns multiplication.

def main():

    a = int(input("Enter first number : "))
    b = int(input("Enter second number : "))

    Mul = lambda a, b: a * b
    print("Multiplication is:", Mul(a, b))

if __name__ == "__main__":
    main()