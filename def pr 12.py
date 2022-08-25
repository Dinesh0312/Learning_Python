#Write a Python function that checks whether a passed string is palindrome or not

def palindrome(str):
    str = str.lower()
    if str == str[::-1]:
        print ("Palindrome")
    else:
        print("Not palindrome")

str = input("enter the string \n")

palindrome(str)