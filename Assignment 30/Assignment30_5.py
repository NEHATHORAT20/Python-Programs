#Search a Word in File
#Problem Statement:
#Write a program which accepts a file name and a word from the user and checks whether that word is present in the file or not.
#Input: Demo.txt Marvellous
#Expected Output: Display whether the word Marvellous is found in Demo.txt or not

import os
import sys

def SearchWord(FileName, Word):
    Ret = os.path.exists(FileName)
    
    if(Ret == True):
        fobj = open(FileName, "r")
        data = fobj.read()
        fobj.close()

        if Word in data:
            return True
        else:
            return False
    else:
        print("File does not exist")

def main():
    FileName = sys.argv[1]
    Word = sys.argv[2]

    Ret = SearchWord(FileName, Word)

    if Ret == True:
        print(f"Word {Word} is found")
    else:
        print(f"Word {Word} is not found")

if __name__ == "__main__":
    main()
