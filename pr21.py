#.From a list pick up all the strings and join them with underscore

l2 = ["one","two","three","four"]
l3 = []
for i in l2:
    l3.append(i)
    l3.append("_")

print(l3)

l3.pop()

print(l3)

l3 = "".join(l3)

print(l3)



