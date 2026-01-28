#Write a program which accept one number and display below pattern.
#Input : 5            Output : *  *  *  *  * 
#                              *  *  *  *  * 
#                              *  *  *  *  * 
#                              *  *  *  *  * 
#                              *  *  *  *  * 

def main():
    No = 0
    No = int(input("Enter Number : "))

    for i in range(No):
        for j in range(No):
            print(" * ", end=" ")
        print()

if __name__ == "__main__":
    main()
