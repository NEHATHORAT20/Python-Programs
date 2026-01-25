#Write a lambda function using map () which accepts a list of numbers and returns a list of squares of each number.

No = [1, 2, 3, 4, 5]

Result = list(map(lambda a: a * a, No))

print("Squares :", Result)