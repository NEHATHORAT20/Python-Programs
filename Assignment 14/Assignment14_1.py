#Write a lambda function which accepts one number and returns square of that number.

Square = lambda a : a * a
print(Square(4))

print("-------------------------")

def main():
    a = int(input("Enter a number : "))

    Square = lambda a : a * a
    print(Square(a))

if __name__ == "__main__":
    main()
