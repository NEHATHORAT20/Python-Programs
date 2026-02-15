#Please follow below rules while designing automation script as
#Accept input through command line or through file.
#Display any message in log file instead of console.
#For separate task define separate function.
#For robustness handle every expected exception.
#Perform validations before taking any action.
#Create user defined modules to store the functionality.

#Design automation script which accept directory name and file extension from user. 
#Display all files with that extension.
#Usage : DirectoryFileSearch.py "Demo" ".txt"
#Demo is name of directory and .txt is the extension that we want to search.

#python3 Assignment31_1.py "Demo" ".txt"

import sys
import os
import time

def DirectoryScanner(Directory, Extension):
    Border = "-"*50
    timestamp = time.ctime()
    Filename = "Demo%s.log" %(timestamp)
    Filename = Filename.replace(" ", "_")
    Filename = Filename.replace(":", "_")

    fobj = open(Filename, "w")

    fobj.write(Border+"\n")
    fobj.write("This is the log file created by Marvellous Automation\n")
    fobj.write("This is a file search automation script\n")
    fobj.write(Border+"\n")

    Ret = os.path.isdir(Directory)

    if(Ret == False):
        fobj.write("There is no such directory\n")
        fobj.close()
        return 
    
    FileCount = 0
    ExtensionFileCount = 0
    
    for FolderName, SubFolderName, FileName in os.walk(Directory):
        for fname in FileName:
            FileCount = FileCount + 1
            fname =  os.path.join(FolderName, fname)

            if(fname.endswith(Extension)):
                ExtensionFileCount = ExtensionFileCount + 1
                fobj.write(fname+"\n")

    fobj.write("Total files scanned : " + str(FileCount) + "\n")
    fobj.write("Total files found with " + Extension + "extension : " + str(ExtensionFileCount) + "\n")
    fobj.write("This log file is created at : " + timestamp + "\n")
    fobj.write(Border+"\n")

    fobj.close()

def main():

    if(len(sys.argv) != 3):
        print("Invalid number of arguments")
        return

    Directory = sys.argv[1]
    Extension = sys.argv[2]

    DirectoryScanner(Directory, Extension)

if __name__ == "__main__":
    main()