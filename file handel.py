
f = open("xyz","w")
f.write("Apple is red\n")
f.close()

f = open("xyz","r+")
print(f.read())

f.write("Sky is blue\n")
f.write("Sun is yellow")

f = open("xyz","w")
f.write("Milk is white")
