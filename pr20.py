#Length of the corosponding word

str = "Rockstar of the Galaxy"
str = str.split()

print(str)

for i in str:
    print(i,":",len(i),end=" , ")

str.pop()

print(str)


length = {}

for i in str:
    c = 0
    for j in i:
        c = c+1
    length[i] = c
print(length)
