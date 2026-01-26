#Design a Python application where multiple threads update a shared variable.
#Use a Lock to avoid race conditions.
#Each thread should increment the shared counter multiple times.
#Display the final value of the counter after all threads complete execution.

import threading

Count = 0

lobj = threading.Lock()

def Update():
    global Count

    for _ in range(1000):
        with lobj:
            Count = Count + 1

def main():
    global Count 

    t1 = threading.Thread(target=Update)
    t2 = threading.Thread(target=Update)
    t3 = threading.Thread(target=Update)

    t1.start()
    t2.start()
    t3.start()

    t1.join()
    t2.join()
    t3.join()

    print("Value of Count is : ", Count)

if __name__ == "__main__":
    main()