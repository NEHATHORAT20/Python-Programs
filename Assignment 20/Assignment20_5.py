#Design a Python application that creates two threads named Thread1 and Thread2.
#Thread1 should display numbers from 1 to 50.
#Thread2 should display numbers from 50 to 1 in reverse order.
#Ensure that:
#Thread2 starts execution only after Thread1 has completed.
#Use appropriate thread synchronization

import threading

def PrintThread1():
    for i in range(1, 51):
        print(i)

def PrintThread2():
    for i in range(50, 0, -1):
        print(i)

def main():
    Thread1 = threading.Thread(target=PrintThread1)
    Thread2 = threading.Thread(target=PrintThread2)

    Thread1.start()
    Thread1.join()
    
    Thread2.start()
    Thread2.join()

if __name__ == "__main__":
    main()
