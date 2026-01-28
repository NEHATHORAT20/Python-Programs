#Write a program which accept one number and display below pattern
#Input : 5            Output : 1  2  3  4  5
#                              1  2  3  4  5
#                              1  2  3  4  5  
#                              1  2  3  4  5  
#                              1  2  3  4  5  

def main():
    No = 0
    No = int(input("Enter Number : "))

    for i in range(1, No + 1):
        for j in range(1, No + 1):
            print(j, end = " ")
        print()

if __name__ == "__main__":
    main()
