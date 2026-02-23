import os
import time
from datetime import datetime
from Process_Monitor import ProcessScan
from Mail import SendEmail

def CreateLog(folder, receiver):

    Border = "-" * 50
    os.makedirs(folder, exist_ok = True)

    timestamp = time.strftime("%Y-%m-%d_%H-%M-%S")
    filename = os.path.join(folder, "Marvellous_%s.log" %timestamp)
    print("Log file gets created with name : ", filename)

    Data = ProcessScan()
    total_processes = len(Data)

    TopCPU = sorted(Data, key=lambda x: x.get("cpu",0), reverse=True)[:5]

    TopMemory = sorted(Data, key=lambda x: x.get("rss",0), reverse=True)[:10]

    TopThreads = sorted(Data, key=lambda x: x.get("thread_count", 0), reverse=True)[:5]

    TopOpenFiles = sorted(Data, key=lambda x: x.get("Open_files") if isinstance(x.get("Open_files"), int) else 0, reverse=True)[:5]

    with open(filename, "w") as fobj:

        fobj.write(Border+"\n")
        fobj.write("---------- Platform Surveillance System ----------\n")
        fobj.write(Border+"\n")
        fobj.write("Log Created at : " + time.ctime()+ "\n")
        fobj.write(Border+"\n")

        fobj.write(f"Top 10 Memory Consuming Processes : {total_processes}\n")
        fobj.write(Border+"\n")

        for info in TopMemory:
            fobj.write("PID : %s\n" %info.get("pid"))
            fobj.write("Process Name : %s\n" %info.get("name"))
            fobj.write("Memory (RSS in MB) : %.2f\n" %info.get("rss"))
            fobj.write("Memory (VMS in MB) : %.2f\n" %info.get("vms"))
            fobj.write("Memory percentage : %.2f\n" %info.get("memory_percent"))
            fobj.write(Border + "\n")

        fobj.write(Border+"\n")
        fobj.write("\nComplete Process Report\n")
        fobj.write(Border + "\n")

        for info in Data:
            fobj.write("PID : %s\n" %info.get("pid"))
            fobj.write("Process Name : %s\n" %info.get("name"))
            fobj.write("CPU %% : %.2f\n" %info.get("cpu"))
            fobj.write("Memory (RSS MB) : %.2f\n" % info.get("rss"))
            fobj.write("Memory (VMS MB) : %.2f\n" % info.get("vms"))
            fobj.write("Memory %% : %.2f\n" % info.get("memory_percent"))
            fobj.write("Thread Count : %s\n" %info.get("thread_count"))
            fobj.write("Open file count : %s\n" %info.get("Open_files"))
            fobj.write("Timestamp : %s\n" % datetime.now())
            fobj.write(Border+"\n")

        fobj.write(Border+"\n")
        fobj.write("----------------- End of File ------------------\n")
        fobj.write(Border+"\n")

        fobj.close()

    sender = "nehajthorat.sits.it@gmail.com"
    app_password = "txoe veuf xpio ibme"

    subject = "Platform Surveillance Report"
    body = f"Total Processes Running : {total_processes}\n"
    
    body += "\nTop 5 CPU Usage Processes:\n"
    for p in TopCPU:
        body += f"{p['name']} (PID: {p['pid']}) - CPU: {p['cpu']:.2f}%\n"

    body += "\nTop 5 Memory Usage Processes:\n"
    for p in TopMemory[:5]:
        body += f"{p['name']} (PID: {p['pid']}) - RSS: {p['rss']:.2f} MB\n"

    body += "\nTop 5 Thread Count Processes:\n"
    for p in TopThreads:
        body += f"{p['name']} (PID: {p['pid']}) - Threads: {p['thread_count']}\n"

    body += "\nTop 5 Open File Processes:\n"
    for p in TopOpenFiles:
        open_files = p['Open_files'] if isinstance(p['Open_files'], int) else 0
        body += f"{p['name']} (PID: {p['pid']}) - Open Files: {open_files}\n"

    SendEmail(sender, app_password, receiver, subject, body, filename)