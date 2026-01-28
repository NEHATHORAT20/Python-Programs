#Write a program which accept number from user and print that number of "*" on screen.
#Input : 5               Output : * * * * *

def main():
    No = 0
    No = int(input("Enter number : "))

    for i in range(No):
        print("*" , end = " ")

if __name__ == "__main__":
    main()
