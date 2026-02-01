#Count Lines in a File
#Problem Statement:
#Write a program which accepts a file name from the user and counts how many lines are present in the file.
#Input: Demo.txt
#Expected Output: Total number of lines in Demo.txt.

import sys
import os

def CountLines(FileName):
    if(os.path.exists(FileName)):
        Count = 0

        fobj = open(FileName, "r")

        Ret = fobj.readlines() 

        for _ in Ret:
            Count = Count + 1

        fobj.close()
        return Count
    else:
        print("No such file exists")

def main():
    FileName = sys.argv[1]

    Ret = CountLines(FileName)
    print(f"Total number of lines in {FileName} :", Ret)

if __name__ == "__main__":
    main()