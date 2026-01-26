#Design a Python application that creates two threads.
#Thread 1 should compute the sum of elements from a list.
#Thread 2 should compute the product of elements from the same list.
#Return the results to the main thread and display them.

import threading

def Sum(Data):
    Result = 0

    for i in range(len(Data)):
        Result = Result + Data[i]

    print("Sum of list elements is :", Result)

def Product(Data):
    Result = 1

    for i in range(len(Data)):
        Result = Result * Data[i]

    print("Product of list elements is :", Result)

def main():
    Data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    Thread1 = threading.Thread(target=Sum, args=(Data,))
    Thread2 = threading.Thread(target=Product, args=(Data,))

    Thread1.start()
    Thread2.start()

    Thread1.join()
    Thread2.join()

if __name__ == "__main__":
    main()