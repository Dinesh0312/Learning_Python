s = input("Enter the String: \n")

s = ''.join(i for i in s.lower() if i.isalnum())

if s == s[::-1]:
    print("True")
else:
    print("False")