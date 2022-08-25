mytuple = ["apple", "banana", "cherry"]

z = iter(mytuple)

print(next(z))
print(z.__next__())
print(next(z))

mystr = "banana"

myit = iter(mystr)

print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))