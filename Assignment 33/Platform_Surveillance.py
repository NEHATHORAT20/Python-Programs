import sys
import time
import schedule
from Log_Creation import CreateLog

def main():

    Border = "-" * 50
    print(Border)
    print("---------- Platform Surveillance System ----------")
    print(Border + "\n")

    if (len(sys.argv) == 2):

        #if sys.argv[1] in ("--h", "--H"):
        if(sys.argv[1] == "--h" or sys.argv[1] == "--H"):

            print(Border + "\n")
            print("This script is used for platform surveillance")
            print("1 : Thread Monitoring")
            print("2 : Open File Monitoring")
            print("3 : Memory Monitoring")
            print("4 : Top 10 Memory Processes")
            print("5 : Periodic Log Generation")
            print(Border + "\n")

        #elif sys.argv[1] in ("--u", "--U"):
        elif(sys.argv[1] == "--u" or sys.argv[1] == "--U"):

            print("Use the automation script as:")
            print("python main.py DirectoryName ReceiverEmail TimeInterval\n")
            print("DirectoryName  : Log Folder Name")
            print("ReceiverEmail  : Receiver Email Address")
            print("TimeInterval   : Time in minutes for scheduling")

        else:
            print("Unable to proceed as there is no such option")
            print("Please use --h or --u to get more details")

    elif len(sys.argv) == 4:

        Directory = sys.argv[1]
        Receiver = sys.argv[2]

        if not sys.argv[3].isdigit():
            print("Time interval must be integer")
            return

        Interval = int(sys.argv[3])

        print("Inside project logic")
        print("Directory Name :" , Directory)
        print("Receiver Email :" , Receiver)
        print("Time Interval  :" , Interval, "minutes")

        schedule.every(Interval).minutes.do(CreateLog, Directory, Receiver)

        print("\nScheduler started successfully...")
        print("Press CTRL + C to stop execution\n")

        try:
            while True:
                schedule.run_pending()
                time.sleep(1)
        except KeyboardInterrupt:
            print(Border)
            print("-------- Platform Surveillance System Stopped --------")
            print(Border + "\n")
            exit()
    else:
        print("Invalid number of command line arguments")
        print("Unable to proceed")
        print("Please use --h or --u to get more details")

    print(Border + "\n")
    print("---------- Thank you for using script -----------")
    print(Border + "\n")

if __name__ == "__main__":
    main()