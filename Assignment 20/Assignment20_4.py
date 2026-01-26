#Design a Python application that creates three threads named Small, Capital, and Digits.
#All threads should accept a string as input.
#The Small thread should count and display the number of lowercase characters.
#The Capital thread should count and display the number of uppercase characters.
#The Digits thread should count and display the number of numeric digits.
#Each thread must also display:
#Thread ID
#Thread Name

import threading

def LowerCase(Name):
    Count = 0
    for ch in Name:
        if ch >= 'a' and ch <= 'z':
            Count += 1

    print("Thread ID :", threading.get_ident())
    print("Thread Name :", threading.current_thread().name)
    print("Small characters :", Count)
    print()

def UpperCase(Name):
    Count = 0
    for ch in Name:
        if ch >= 'A' and ch <= 'Z':
            Count += 1

    print("Thread ID :", threading.get_ident())
    print("Thread Name :", threading.current_thread().name)
    print("Capital characters :", Count)
    print()

def NumericDigit(Name):
    Count = 0
    for ch in Name:
        if ch >= '0' and ch <= '9':
            Count += 1

    print("Thread ID :", threading.get_ident())
    print("Thread Name :", threading.current_thread().name)
    print("Digits :", Count)
    print()

def main():
    Name = input("Enter string : ")

    Small = threading.Thread(target=LowerCase, args=(Name,), name="Small")
    Capital = threading.Thread(target=UpperCase, args=(Name,), name="Capital")
    Digits = threading.Thread(target=NumericDigit, args=(Name,), name="Digits")

    Small.start()
    Capital.start()
    Digits.start()

    Small.join()
    Capital.join()
    Digits.join()

if __name__ == "__main__":
    main()
