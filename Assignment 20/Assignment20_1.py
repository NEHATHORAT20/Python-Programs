#Design a Python application that creates two separate threads named Even and Odd.
#The Even thread should display the first 10 even numbers.
#The Odd thread should display the first 10 odd numbers.
#Both threads should execute independently using the threading module.
#Ensure proper thread creation and execution.

import threading

def DisplayEven():
    for i in range(2, 21):
        if i % 2 == 0:
            print(i)
        
def DisplayOdd():
    for i in range(1, 21):
        if i % 2 != 0:
            print(i)

def main():
    Even = threading.Thread(target=DisplayEven)
    Odd = threading.Thread(target=DisplayOdd)

    Even.start()
    Odd.start()

    Even.join()
    Odd.join()    

if __name__ == "__main__":
    main()