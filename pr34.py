l2 = ["one","two","three","four"]

l3 = ""

for i in range(0,len(l2)):
    l3 = l2[i] + "_"

l3 = l3.split('_')

print(l3)