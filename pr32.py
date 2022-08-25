s1 = input("Enter the sub string")
s2 = input("Enter the main string")

k = []
for i in s1:
    for j in s2:
        if j == i and j not in k:
            k.append(j)
k = "".join(k)

if k == s1:
    print("true")
else:
    print("false")


if s1 in s2:
    print("True")
else:
    print("false")
