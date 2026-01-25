#Write a lambda function using filter () which accepts a list of numbers and returns a list of odd numbers.

No = [1, 2, 3, 4, 5, 6]

Result = list(filter(lambda b: b % 2 != 0, No))

print("Odd Numbers:", Result)