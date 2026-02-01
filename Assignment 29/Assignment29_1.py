#Check File Exists in Current Directory
#Problem Statement:
#Write a program which accepts a file name from the user and checks whether that file exists in the current directory or not.
#Input: Demo.txt
#Expected Output: Display whether Demo. txt exists or not.

import os

def main():
    FileName = input("Enter the file name : ")

    Ret = os.path.exists(FileName)

    if(Ret == True):
        print(f"{FileName} exists")
    else:
        print("No such file in this directory")

if __name__ == "__main__":
    main()