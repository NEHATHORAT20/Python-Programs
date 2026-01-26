#Design a Python application that creates two threads named EvenFactor and OddFactor.
#Both threads should accept one integer number as a parameter.
#The EvenFactor thread should:
#1Identify all even factors of the given number.
#2Calculate and display the sum of even factors.
#The OddFactor thread should:
#1Identify all odd factors of the given number.
#2Calculate and display the sum of odd factors.
#After both threads complete execution, the main thread should display the message:
#"Exit from main"

import threading

def SumEven(No):
    Sum = 0

    for i in range(1, No+1):
        if No % i == 0:
            if i % 2 == 0:
                Sum = Sum + i

    print("Sum of Even :", Sum)

def SumOdd(No):
    Sum = 0

    for i in range(1, No+1):
        if No % i == 0:
            if i % 2 != 0:
                Sum = Sum + i

    print("Sum of Odd :", Sum)

def main():
    No = 0
    No = int(input("Enter number  : "))

    EvenFactor = threading.Thread(target=SumEven, args=(No,))
    OddFactor = threading.Thread(target=SumOdd, args=(No,))

    EvenFactor.start()
    OddFactor.start()

    EvenFactor.join()
    OddFactor.join()

    print("Exit from main")

if __name__ == "__main__":
    main()