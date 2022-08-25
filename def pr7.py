#Write a Python function to check whether a number falls in a given range


def check(n):
    if n in range(s_r,e_r):
        print ("Number falls in a given range")
    else:
        print("number not falls in a given range")

s_r = int(input("Enter the start range : "))
e_r = int(input("Enter the end range : "))

n = int(input("Enter the number : "))

check(n)