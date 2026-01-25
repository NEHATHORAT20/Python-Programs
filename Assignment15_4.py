#Write a lambda function using reduce () which accepts a list of numbers and returns the addition of all elements.

from functools import reduce

No = [1, 2, 3, 4, 5]

Result = reduce(lambda a, b: a + b, No)

print("Addition:", Result)