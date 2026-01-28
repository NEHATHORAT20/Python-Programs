#Write a lambda function which accepts two numbers and returns minimum number.

Min = lambda a,b: min(a,b)
print(Min(10,20))

print("-------------------------------------")

def main():
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))

    Min = lambda a,b: min(a,b)
    print(Min(a,b))

if __name__ == "__main__":
    main()
