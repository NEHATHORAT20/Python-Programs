#Please follow below rules while designing automation script as
#Accept input through command line or through file.
#Display any message in log file instead of console.
#For separate task define separate function.
#For robustness handle every expected exception.
#Perform validations before taking any action.
#Create user defined modules to store the functionality.

#Design automation script which accept directory name and display checksum of all files.
#Usage : DirectoryChecksum.py "Demo"
#Demo is name of directory.

import sys
import os
import hashlib

def CalculateCheckSum(Filename):
        
        fobj = open(Filename, "rb")

        hobj = hashlib.md5()

        Buffer = fobj.read(1024)

        while(len(Buffer) > 0):
            hobj.update(Buffer)
            Buffer = fobj.read(1024)

        fobj.close()

        return hobj.hexdigest()

def DirectoryCheckSum(Directory):

    fobj = open("CheckSumLog.txt" , "w")

    if not os.path.exists(Directory):
        fobj.write("Directory does not exists\n")
        return
    
    if not os.path.isdir(Directory):
        fobj.write("This is not a directory\n")
        return
    
    FileCount = 0

    for FolderName, SubFolderName, FileName in os.walk(Directory):
        for fname in FileName:
            fname = os.path.join(FolderName, fname)

            CheckSum = CalculateCheckSum(fname)
            fobj.write(f"File name : {fname} CheckSum : {CheckSum}" + "\n")
            FileCount = FileCount + 1

    fobj.write("\nTotal files scanned : " + str(FileCount) + "\n")

    fobj.close()

def main():

    if(len(sys.argv) != 2):
        print("Invalid number of arguments")
        return

    Directory = sys.argv[1]

    DirectoryCheckSum(Directory)

if __name__ == "__main__":
    main()