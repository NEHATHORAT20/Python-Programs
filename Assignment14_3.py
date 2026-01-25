#Write a lambda function which accepts two numbers and returns maximum number.

Max = lambda a,b: max(a,b)
print(Max(10,20))

print("-----------------------------------------")

def main():
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))

    Max = lambda a,b: max(a,b)
    print(Max(a,b))

if __name__ == "__main__":
    main()