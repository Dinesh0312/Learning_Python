#valid palindrom


def palen(n):
    if n == n[::-1]:
        print("it is palindrom")
    else:
        print("it is not a palindrom")


n = input("enter the string\n")

palen(n)