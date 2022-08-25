s = input("Enter your String: \n")
s = s.split()

z = []

for i in s:
    if i.isalnum() and not i.isalpha() and not i.isnumeric():
        z.append(i)

z = " ".join(z)

print(z)