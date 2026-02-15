#Design automation script which accept two directory names. 
#Copy all files from first directory into second directory. 
#Second directory should be created at run time.
#Usage : DirectoryCopy.py "Demo" "Temp"
#Demo is name of directory which is existing and contains files in it. 
#We have to create new Directory as Temp and copy all files from Demo to Temp.

# python Assignment31_3.py Demo Temp

import sys
import os
import time

def DirectoryCopy(Directory1, Directory2):

    Border = "-"*50
    timestamp = time.ctime()
    Filename = "Demo%s.log" %(timestamp)
    Filename = Filename.replace(" ", "_")
    Filename = Filename.replace(":", "_")

    fobj = open(Filename, "w")

    fobj.write(Border+"\n")
    fobj.write("This is the log file created by Marvellous Automation\n")
    fobj.write("This is to copy file to another directory\n")
    fobj.write(Border+"\n") 

    Ret = False

    Ret = os.path.isdir(Directory1)

    if(Ret == False):
        fobj.write("There is no such directory")
        return
    
    os.makedirs(Directory2)

    FileCount = 0

    for FolderName, SubFolderName, FileName in os.walk(Directory1):

        for fname in FileName:
            fname = os.path.join(FolderName, fname)
            FileCount = FileCount + 1
            
            if os.path.isfile(fname):

                NewPath = os.path.join(Directory2, os.path.basename(fname))

                fobj1 = open(fname, "r")
                File = fobj1.read()

                fobj2 = open(NewPath, "w")
                fobj2.write(File)

                fobj1.close()
                fobj2.close()

    fobj.write("Total files Copied : " +str(FileCount)+ "\n")
    fobj.write("This log file is created at : " +timestamp+ "\n")
    fobj.write(Border + "\n")

    fobj.close()

def main():
    
    if(len(sys.argv) != 3):
        print("Invalid number of arguments")
        return
    
    Directory1 = sys.argv[1]
    Directory2 = sys.argv[2]

    DirectoryCopy(Directory1, Directory2)

if __name__ == "__main__":
    main()