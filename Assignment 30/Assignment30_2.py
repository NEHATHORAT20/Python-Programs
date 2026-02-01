#Count Words in a File
#Problem Statement:
#Write a program which accepts a file name from the user and counts the total number of words in that file.
#Input: Demo.txt
#Expected Output: Total number of words in Demo.txt.

import sys
import os

def CountWords(FileName):
    if(os.path.exists(FileName)):
        Count = 1

        fobj = open(FileName, "r")

        Ret = fobj.read()
        fobj.close()

        for word in Ret:
            if(word == " "):
                Count = Count + 1

        return Count
    else:
        print("No such file exists in directory")

def main():
    FileName = sys.argv[1]

    Ret = CountWords(FileName)
    print(Ret)

if __name__ == "__main__":
    main()