#Write a program which accepts one character and checks whether it is vowel or consonant.

#Input: a
#Output: Vowel

def Vowel(ch):
    if ch in ('a' , 'e' , 'i' , 'o' , 'u' ,
              'A' , 'E' , 'I' , 'O' , 'U'):
        print("Vowel")
    else:
        print("Consonant")

Vowel('a')