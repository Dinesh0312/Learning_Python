#Write a Python program to find if a given string starts with a given character using Lambda.

starts_with = lambda x: True if x.startswith('p') else False

n = input("Enter the string : ")

print(starts_with(n))

ends_with = lambda x: True if x.endswith('p') else False

x = input("Enter the string : ")

print(starts_with(x))