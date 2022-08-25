#Find the last position of a given substring

s1 = "Emma is a data scientist who knows Python. Emma works at google."
s2 = 'Emma'

if s2 in s1:
    print("Sub-string found",end=" ")
else:
    print("Sub-string not exist")

z = s1.rindex(s2)

print("on position", z)

