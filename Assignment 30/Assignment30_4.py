#Copy File Contents into Another File
#Problem Statement:
#Write a program which accepts two file names from the user.
#First file is an existing file
#Second file is a new file
#Copy all contents from the first file into the second file.
#Input: ABC.txt Demo.txt
#Expected Output: Contents of ABC.txt copied into Demo.txt.

import os
import sys

def main():
    FileName = sys.argv[1]

    Ret = os.path.exists(FileName)

    if(Ret == True):
        fobj = open(FileName, "r")

        Data = fobj.read()

        fobj1 = open("Demo.txt", "w")
        fobj1.write(Data)

        fobj.close()
        fobj1.close()

if __name__ == "__main__":
    main()