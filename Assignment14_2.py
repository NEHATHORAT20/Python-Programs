#Write a lambda function which accepts one number and returns cube of that number.

Cube = lambda a : a**3 
print(Cube(4))

print("-------------------------------")

def main():
    a = int(input("Enter a number : "))

    Cube = lambda a : a * a * a
    print(Cube(a))

if __name__ == "__main__":
    main()