#String characters balance Test

s1 = input("Enter the Sub - String that need to be verified: \n")
s2 = input("Enter the String: \n")

k = []
for i in s1: # S1 = Y n z
    for j in s2: # s2 = PYnative
        if j == i and j not in k:
            k.append(j)
k = "".join(k)

if k == s1:
    print("True")
else:
    print("False")


