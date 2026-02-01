#Display File Contents
#Problem Statement:
#Write a program which accepts a file name from the user, opens that file, and displays the entire contents on the console.
#Input: Demo.txt
#Expected Output: Display contents of Demo. txt on console.

import os

def main():
    FileName = input("Enter the file name : ")

    Ret = os.path.exists(FileName)

    if(Ret == True):
        fobj = open(FileName, "r")
        
        Data = fobj.read()
        print("File contents : ", Data)

        fobj.close()

    else:
        print("No such file exists in this directory")

if __name__ == "__main__":
    main()