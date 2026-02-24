import sys
import time
import schedule
import logging

from Backup_Module import BackupFiles, make_zip
from Email_Module import SendEmail
from Log_Module import CreateLog, Update, Display
from Restore_Module import RestoreBackup

def MarvellousDataShield(Source):

    log_file = CreateLog()
    logging.info("Backup started")

    backup_folder = "MarvellousBackup"

    files = BackupFiles(Source, backup_folder)
    zip_file = make_zip(backup_folder)

    logging.info("Backup completed Succesfully")
    logging.info("Files copied: %d", len(files))
    logging.info("Zip created: %s", zip_file)

    for name in files:
        logging.info("Copied filename: %s", name)

    Update(len(files), zip_file)

    logging.info("History updated successfully")

    return log_file, zip_file

def BackupEmail(Source):
    log_file, zip_file = MarvellousDataShield(Source)
    SendEmail(log_file, zip_file)

def main():

    Border = "-"*50
    print(Border)
    print("--------- Marvellous Data sheild System ----------")
    print(Border+"\n")

    if(len(sys.argv) == 2):

        if(sys.argv[1] == "--h" or sys.argv[1] == "--H"):
            print("1 : Takes auto backup at given time")
            print("2 : Backup only new and updated files")
            print("3 : Create archive of backup periodically")

        elif(sys.argv[1] == "--u" or sys.argv[1] == "--U"):
            print("Use the automation script as")
            print("ScriptName.py TimeInterval SourceDirectory")
            print("TimeInterval : Time in minutes")
            print("SourceDirectory : Directory to backup")

        elif(sys.argv[1] == "--history" or sys.argv[1] == "--HISTORY"):
            Display()

        else:
            print("Unable to proceed as there is no such option")
            print("Please use --h or --u for details")

    elif(len(sys.argv) == 3):

        try:
            interval = int(sys.argv[1])
            source = sys.argv[2]

            schedule.every(interval).minutes.do(BackupEmail, source)

            print("Data shield started successfully")
            print("Time interval in minutes:", interval)
            print("Press Ctrl + C to stop execution")

            while True:
                schedule.run_pending()
                time.sleep(1)

        except KeyboardInterrupt:
            print("\nProgram stopped successfully")
            exit()

    elif(len(sys.argv) == 4 and sys.argv[1] == "--restore"):

        RestoreBackup(sys.argv[2], sys.argv[3])
        print("Restore operation completed")

    else:
        print("Invalid number of command line arguments")
        print("Please use --h or --u to get details")

    print(Border)
    print("--------- Thank you for using our script ---------")
    print(Border+"\n")

if __name__ == "__main__":
    main()