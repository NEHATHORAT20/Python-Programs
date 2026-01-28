#Write a program which accepts one number and prints binary equivalent.

def Binary(No):

    Binary = " "
    while No > 0:
        Binary = str(No % 2) + Binary
        No = No // 2
    return Binary

Result = Binary(11)
print("Binary : ", Result)
