#Write a lambda function using filter () which accepts a list of numbers and returns a list of even numbers.

No = [1, 2, 3, 4, 5, 6]

Result = list(filter(lambda x: x % 2 == 0, No))

print("Even Numbers:", Result)