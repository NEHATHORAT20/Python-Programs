#Write a Python program to implement a class named BankAccount with the following requirements:
#The class should contain two instance variables:
#Name (Account holder name)
#Amount (Account balance)
#The class should contain one class variable:
#ROI (Rate of Interest), initialized to 10.5
#Define a constructor(__init__) that accepts Name and initial Amount.
#Implement the following instance methods:
#Display ( ) - displays account holder name and current balance
#Deposit ( ) - accepts an amount from the user and adds it to balance
#Withdraw ( ) - accepts an amount from the user and subtracts it from balance
#(Ensure withdrawal is allowed only if sufficient balance exists)
#CalculateInterest ( ) - calculates and returns interest using formula:
#Interest = (Amount * ROI) / 100
#Create multiple objects and demonstrate all methods.

class BankAccount:

    ROI = 10.5

    def __init__(self, A, B):
        self.Name = A
        self.Amount = B

    def Display(self):
        print(f"Account holder Name is {self.Name} and current balance is {self.Amount}")

    def Deposit(self):
        Amount = float(input("Enter amount for deposit : "))
        self.Amount = self.Amount + Amount

    def Withdraw(self):
        Withdraw = int(input("Enter amount for withdraw : "))
        
        if(self.Amount >= Withdraw):
            self.Amount = self.Amount - Withdraw
        else:
            print("Insufficient balance in your acoount")

    def CalculateInterest(self):
        Interest = (self.Amount * BankAccount.ROI) / 100
        print("ROI on amount :", Interest)
    
obj1 = BankAccount("Yash", 800000)
obj1.Display()
obj1.Deposit()
obj1.Withdraw()
obj1.CalculateInterest()

obj2 = BankAccount("Neha", 900000)
obj2.Display()
obj2.Deposit()
obj2.Withdraw()
obj2.CalculateInterest()