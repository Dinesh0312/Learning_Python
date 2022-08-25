str = "abcccccdeegg"

str = list(str)

print(str)

l1 = []

for i in str:
    if i not in l1:
        l1.append(i)
print(l1)

for i in l1:
    c = 0
    for j in str:
        if i == j:
            c +=1
    print(i,":",c)

dict = {}
for i in l1:
    dict[i] = str.count(i)
print(dict)