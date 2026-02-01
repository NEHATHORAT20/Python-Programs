#Display File Line by Line
#Problem Statement:
#Write a program which accepts a file name from the user and displays the contents of the file line by line on the screen.
#Input: Demo.txt
#Expected Output: Display each line of Demo.txt one by one.

import sys
import os

def DisplayLine(FileName):
    if(os.path.exists(FileName)):
        fobj = open(FileName, "r")

        Ret = fobj.readlines()

        for line in Ret:
            print(line)
    else:
        print("No such file exists")

def main():

    FileName = sys.argv[1]

    DisplayLine(FileName)

if __name__ == "__main__":
    main()