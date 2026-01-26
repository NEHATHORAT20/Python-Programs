#Design a Python application that creates two threads named EvenList and OddList.
#Both threads should accept a list of integers as input.
#The EvenList thread should:
#1Extract all even elements from the list.
#2Calculate and display their sum.
#The OddList thread should:
#1Extract all odd elements from the list.
#2Calculate and display their sum.
#Threads should run concurrently.

import threading
from functools import reduce

def EvenSum(Data):
    FData = list(filter((lambda No : No % 2 == 0), Data))

    RData = reduce((lambda No1, No2: No1 + No2), FData)

    print("Even Sum :", RData)
    

def OddSum(Data):
    FData = list(filter((lambda No : No % 2 != 0), Data))

    RData = reduce((lambda No1, No2: No1 + No2), FData)

    print("Odd Sum :", RData)

def main():
    Data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]  

    EvenList = threading.Thread(target=EvenSum, args=(Data,))
    OddList = threading.Thread(target=OddSum, args=(Data,))

    EvenList.start()
    OddList.start()

    EvenList.join()
    OddList.join()

if __name__ == "__main__":
    main()