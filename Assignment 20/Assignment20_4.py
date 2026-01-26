#Design a Python application that creates three threads named Small, Capital, and Digits.
#All threads should accept a string as input.
#The Small thread should count and display the number of lowercase characters.
#The Capital thread should count and display the number of uppercase characters.
#The Digits thread should count and display the number of numeric digits.
#Each thread must also display:
#Thread ID
#Thread Name

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