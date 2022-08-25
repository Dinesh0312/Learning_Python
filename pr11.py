v1 = int(input("enter value_1 "))
v2 = int(input("enter value_1 "))
v3 = int(input("enter value_1 "))

if v1>=v2 and v1>=v3:
    greatest = v1
elif v2>=v3 and v2>=v1:
    greatest = v2
else:
    greatest = v3

print(greatest, " : is the greatest number among three")