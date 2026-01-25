#Write a lambda function using filter () which accepts a list of strings and returns a list of strings having length greater than 5.

Names = ["Python", "Java", "Angular", "C", "Javascript" , "Marvellous"]

Result = list(filter(lambda x: len(x) > 5, Names))

print("Strings with length > 5 : " , Result)