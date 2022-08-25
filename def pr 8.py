#Write a Python function that accepts a string and calculate the number of upper case letters and lower case letters

def count(str):
    upper = 0
    lower = 0
    for i in str:
        if i.isupper():
            upper += 1
        if i.islower():
            lower += 1
    return upper,lower

str = 'The quick Brow Fox'

result = count(str)
print("Upper case letters {} and lower case letters {} ".format(result[0], result[1]))