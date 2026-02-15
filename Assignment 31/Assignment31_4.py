#Design automation script which accept two directory names and one file extension.
#Copy all files with the specified extension from first directory into second directory.
#Second directory should be created at run time.
#Usage : DirectoryCopyExt.py "Demo" "Temp" ".exe"
#Demo is name of directory which is existing and contains files in it. 
#We have to create new Directory as Temp and copy all files with extension .exe from Demo to Temp.

# python Assignment31_4.py Demo Hello .doc   

import sys
import os
import time

def DirectoryCopyExt(Directory1, Directory2, Extension):
    Border = "-"*50
    timestamp = time.ctime()
    Filename = "Demo%s.log" %(timestamp)
    Filename = Filename.replace(" " , "_")
    Filename = Filename.replace(":" , "_")

    fobj = open(Filename, "w")

    fobj.write(Border+"\n")
    fobj.write("This is the log file created by Marvellous Automation\n")
    fobj.write("This script copies files to another directory\n")
    fobj.write(Border+"\n")

    if not os.path.isdir(Directory1):
        fobj.write("There is no such directrory\n")
        fobj.close()
        return 
    
    if not os.path.exists(Directory2):
        os.mkdir(Directory2)
    else:
        fobj.write("Destination directory already exists\n")

    FileCount = 0
    CopyFileCount = 0

    for FolderName, SubFolderName, FileName in os.walk(Directory1):
        for fname in FileName:
            FileCount = FileCount + 1
            fname = os.path.join(FolderName, fname)

            if(fname.endswith(Extension)):
                CopyFile = os.path.join(Directory2, os.path.basename(fname))

                fobj1 = open(fname, "rb")
                File = fobj1.read()

                fobj2 = open(CopyFile, "wb")
                fobj2.write(File)

                fobj1.close()
                fobj2.close()

                CopyFileCount = CopyFileCount + 1
                fobj.write("Copied: " + fname + "\n")

    fobj.write("Total files Scanned : " +str(FileCount)+ "\n")
    fobj.write("Total files Copied : " +str(CopyFileCount)+ "\n")
    fobj.write("This log file is created at : " +timestamp+ "\n")
    fobj.write(Border+"\n")

    fobj.close()

def main():

    if(len(sys.argv) != 4):
        print("Invalid number of arguments")
        return
    
    Directory1 = sys.argv[1]
    Directory2 = sys.argv[2]
    Extension = sys.argv[3] 

    DirectoryCopyExt(Directory1, Directory2, Extension)

if __name__ == "__main__":
    main()