#Please follow below rules while designing automation script as:
# 1. Accept input through command line or through file.
# 2. Display any message in log file instead of console.
# 3. For separate task define separate function.
# 4. For robustness handle every expected exception.
# 5. Perform validations before taking any action.
# 6. Create user defined modules to store the functionality.

#Please add below features in our project named as Marvellous Data Shield System
#1. Logging System
#Create a Logs/ folder
#Store:
#.Backup start time
#.Files copied
#.Zip file name
#.Errors (if any)

#2. Email Notification
#Send an email after backup completion
#Attach:
#.Log file
#.Zip file name

#3. Restore Feature
#Add a command:
#.python Script.py --restore ZipFileName Destination
#Extract backup to given directory

#4. Exclude Files / Folders
#Ignore:
# .tmp, .log, .exe
#or user-defined extensions

#5. Backup History Tracker
#Maintain a file containing:
#.Date
#.Number of files
#.Zip size
#Display history using:
#.python Script.py --history

import os
import time
import logging
from datetime import datetime

def CreateLog():
    if not os.path.exists("Logs"):
        os.makedirs("Logs" , exist_ok = True)

    timestamp = time.strftime("%Y-%m-%d_%H-%M-%S")
    log_file = os.path.join("Logs", "BackupLog" + timestamp + ".log")

    logger = logging.getLogger()
    logger.setLevel(logging.INFO)

    if logger.hasHandlers():
        logger.handlers.clear()

    handler = logging.FileHandler(log_file)
    formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
    handler.setFormatter(formatter)

    logger.addHandler(handler)

    return log_file

def Update(file_count, zip_file):

    FileHistory = "BackupHistory.txt"
    size = os.path.getsize(zip_file)

    with open(FileHistory, "a") as fobj:
        fobj.write(f"{datetime.now()} | Files {file_count} | Size {size} bytes\n")


def Display():

    FileHistory = "BackupHistory.txt"

    if not os.path.exists(FileHistory):
        print("No backup history available.")
        return

    print("----------- Backup History -----------")

    if os.path.exists(FileHistory):
        with open(FileHistory, "r") as hobj:
            print(hobj.read())