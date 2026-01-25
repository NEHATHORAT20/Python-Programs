#Write a lambda function using filter () which accepts a list of numbers and returns a list of numbers divisible by both 3 and 5.

Value = [10, 15, 30, 25, 9, 45]

Result = list(filter(lambda No: No % 3 == 0 and No % 5 == 0, Value))

print("Divisible by 3 and 5:", Result)