#Copy File Contents into a New File (Command Line)
#Problem Statement:
#Write a program which accepts an existing file name through command line arguments, creates a new file named Demo. txt, and copies all contents from the given file into Demo. txt.
#Input (Command Line): ABC.txt
#Expected Output: Create Demo. txt and copy contents of ABC. txt into Demo.txt.

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