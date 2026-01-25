#Write a lambda function using filter () which accepts a list of numbers and returns the count of even numbers.

No = [1, 2, 3, 4, 5, 6, 7, 8]

Result = len(list(filter(lambda x: x % 2 == 0, No)))

print("Count of Even Numbers : ", Result)