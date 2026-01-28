#Write a Python program to implement a class named Arithmetic with the following characteristics:
#The class should contain two instance variables: Value1 and Value2.
#Define a constructor (__init__) that initializes all instance variables to 0.
#Implement the following instance methods:
#Accept ( ) - accepts values for Value1 and Value2 from the user.
#Addition ( ) - returns the addition of Value1 and Value2.
#Subtraction ( ) - returns the subtraction of Value1 and Value2.
#Multiplication () -returns the multiplication of Value1 and Value2.
#Division () -returns the division of Value1 and Value2 (handle division by zero properly).
#Create multiple objects of the Arithmetic class and invoke all the instance methods.

class Arithmetic:

    def __init__(self):
        self.Value1 = 0
        self.Value2 = 0

    def Accept(self):
        self.Value1 = int(input("Enter value1 : "))
        self.Value2 = int(input("Enter Value2 : "))

    def Addition(self):
        return self.Value1 + self.Value2
    
    def Subtraction(self):
        return self.Value1 - self.Value2
    
    def Multiplication(self):
        return self.Value1 * self.Value2
    
    def Division(self):
        try:
            return self.Value1 / self.Value2
        except ZeroDivisionError as zobj:
            return zobj

        # if(self.Value2 != 0):
        #     return self.Value1 / self.Value2
        # return "Cannot divided by zero"

obj1 = Arithmetic()
obj1.Accept()
print("Addition :", obj1.Addition())
print("Subtraction :", obj1.Subtraction())
print("Multiplication :", obj1.Multiplication())
print("Division :", obj1.Division())

obj2 = Arithmetic()
obj2.Accept()
print("Addition :", obj2.Addition())
print("Subtraction :", obj2.Subtraction())
print("Multiplication :", obj2.Multiplication())
print("Division :", obj2.Division())

obj3 = Arithmetic()
obj3.Accept()
print("Addition :", obj3.Addition())
print("Subtraction :", obj3.Subtraction())
print("Multiplication :", obj3.Multiplication())
print("Division :", obj3.Division())