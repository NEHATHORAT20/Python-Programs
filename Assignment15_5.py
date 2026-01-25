#Write a lambda function using reduce () which accepts a list of numbers and returns the maximum element.

from functools import reduce

No = [10, 5, 20, 8]

Result = reduce(lambda a, b: a if a > b else b, No)

print("Maximum:", Result)