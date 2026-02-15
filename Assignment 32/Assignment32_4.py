#Design automation script which accept directory name and delete all duplicate files from that directory.
#Write names of duplicate files from that directory into log file named as Log2.txt.
#Log2.txt file should be created into current directory. 
#Display execution time required for the script.
#Usage : DirectoryDusplicateRemoval.py "Demo"
#Demo is name of directory.

import sys
import os
import hashlib
import time

def CalculateCheckSum(fname):
    fobj = open(fname, "rb")

    hobj = hashlib.md5()

    Buffer = fobj.read(1024)

    while(len(Buffer) > 0):
        hobj.update(Buffer)
        Buffer = fobj.read(1024)

    fobj.close()

    return hobj.hexdigest()

def FindDuplicate(Directory):
    
    Duplicate = {}
    
    for FolderName, SubFolderName, FileName in os.walk(Directory):
        for fname in FileName:
            fname = os.path.join(FolderName, fname)

            CheckSum = CalculateCheckSum(fname)

            if CheckSum in Duplicate:
                Duplicate[CheckSum].append(fname)
            else:
                Duplicate[CheckSum] = [fname]

    return Duplicate

def DirectoryDuplicateRemove(Directory):
    start_time = time.time()

    Border = "-" * 50
    timestamp = time.ctime()

    fobj = open("Log2.txt", "w")

    fobj.write(Border + "\n")
    fobj.write("This is the log file created using python\n")
    fobj.write("This script deletes duplicate files\n")
    fobj.write(Border + "\n")

    if not os.path.exists(Directory):
        fobj.write("No such directory exists\n")
        fobj.close()
        return 
    
    if not os.path.isdir(Directory):
        fobj.write("This is not a directory\n")
        fobj.close()
        return
    
    MyDict = FindDuplicate(Directory)

    Result = list(filter(lambda x: len(x) > 1, MyDict.values()))
    
    Count = 0
    Cnt = 0

    for value in Result:
        for subvalue in value:
            Count = Count + 1
            if(Count > 1):
                fobj.write("Deleted file : "+subvalue+"\n")
                os.remove(subvalue)
                Cnt = Cnt + 1

        Count = 0

    end_time = time.time()

    Execution_time = end_time - start_time

    fobj.write("Total duplicate files : " +str(Cnt)+"\n")
    fobj.write("Execution time : " +str(Execution_time)+"\n")
    fobj.write("This log file is created at : " +timestamp+"\n")
    fobj.write(Border+"\n")
        
    fobj.close()

def main():

    if(len(sys.argv) != 2):
        print("Invalid number of arguments")
        return 
    
    Directory = sys.argv[1]

    DirectoryDuplicateRemove(Directory)

if __name__ == "__main__":
    main()