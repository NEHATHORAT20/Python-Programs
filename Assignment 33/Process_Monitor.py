import psutil
import time

def ProcessScan():

    Processes = []

    for proc in psutil.process_iter():
        try:
            proc.cpu_percent()
        except:
            pass

    time.sleep(1)

    for proc in psutil.process_iter():
        try:
            info = proc.as_dict(attrs=["pid", "name"])

            mem = proc.memory_info()
            info["rss"] = mem.rss / (1024*1024)
            info["vms"] = mem.vms / (1024*1024)
            info["memory_percent"] = proc.memory_percent()

            info["cpu"] = proc.cpu_percent()
            info["thread_count"] = proc.num_threads()

            try:
                info["Open_files"] = len(proc.open_files())
            except psutil.AccessDenied:
                info["Open_files"] = "Access Denied"
            except:
                info["Open_files"] = "NA"
                
            try:
                info["create_time"] = time.strftime("%Y-%m-%d %H-%M-%S", time.localtime(proc.create_time()))

            except:
                info["create_time"] = "NA"

            Processes.append(info)

        except (psutil.NoSuchProcess , psutil.AccessDenied , psutil.ZombieProcess):
            pass

    return Processes