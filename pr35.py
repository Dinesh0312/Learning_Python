#Replace each special symbol with #

s1 = input("Enter Your String: \n")

l1 = []

for i in s1:
    if i.isalpha() or i.isnumeric() or i.isspace():
        l1.append(i)
    else:
        l1.append('#')

l1 = "".join(l1)

print(l1)

