#Design automation script which accept directory name and two file extensions from user.
#Rename all files with first file extension with the second file extention.
#Usage : DirectoryRename.py "Demo" ".txt" ".doc"
#Demo is name of directory and .txt is the extension that we want to search and rename with .doc.
#After execution this script each .txt file gets renamed as .doc.

#python Assignment31_2.py Demo .txt .doc

import sys
import os
import time

def DirectoryRename(Directory, Extension1, Extension2):
    Border = "-"*50
    timestamp = time.ctime()
    Filename = "Demo%s.log" %(timestamp)
    Filename = Filename.replace(" ", "_")
    Filename = Filename.replace(":", "_")

    fobj = open(Filename, "w")

    fobj.write(Border+"\n")
    fobj.write("This is the log file created by Marvellous Automation\n")
    fobj.write("This script changes file extention\n")
    fobj.write(Border+"\n")

    Ret = False 

    Ret = os.path.isdir(Directory)

    if(Ret == False):
        fobj.write("There is no such directory\n")
        fobj.close()
        return 
    
    FileCount = 0
    ChangeFileCount = 0

    for FolderName, SubFolderName, FileName in os.walk(Directory):
        for fname in FileName:
            FileCount = FileCount + 1
            fname =  os.path.join(FolderName, fname)

            if fname.endswith(Extension1):
                try:
                    file, ext = os.path.splitext(fname)
                    NewName = file + Extension2
                    os.rename(fname, NewName)

                    ChangeFileCount = ChangeFileCount + 1
                    fobj.write("Renamed: " + fname + " -> " + NewName + "\n")
                except:
                    return

    fobj.write("Total files scanned : " +str(FileCount)+"\n")
    fobj.write("Total files extension changed : " +str(ChangeFileCount)+"\n")
    fobj.write("This log file is created at : " +timestamp+"\n")
    fobj.write(Border+"\n")

    fobj.close()
                
def main():
    
    if(len(sys.argv) != 4):
        print("Invalid number of arguments")
        return
    
    Directory = sys.argv[1]
    Extension1 = sys.argv[2]
    Extension2 = sys.argv[3]

    DirectoryRename(Directory, Extension1, Extension2)

if __name__ == "__main__":
    main()