#Frequency of a String in File
#Problem Statement:
#Write a program which accepts a file name and one string from the user and returns the frequency (count of occurrences) of that string in the file.
#Input: Demo.txt Marvellous
#Expected Output: Count how many times "Marvellous" appears in Demo. txt.

import os 
import sys

def CountOccurrences(FileName, String):
    if(os.path.exists(FileName)):
        Count = 0
        fobj = open(FileName, "r")

        Ret = fobj.read()
        fobj.close()
        
        Count = Ret.count(String)
        return Count
    
    else:
        print("No such file exists")
        return 0 

def main():
    FileName = sys.argv[1]
    String = sys.argv[2]

    Ret = CountOccurrences(FileName, String)
    print(Ret)
    
if __name__ == "__main__":
    main()