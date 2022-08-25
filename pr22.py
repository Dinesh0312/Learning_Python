str = 'jump zoo zoo jump Taxi Aeroplane Taxi zoo'

str = str.split()

l1 = []

for i in str:
    if i not in l1:
        l1.append(i)
print(l1)

for i in l1:
    print(i, str.count(i))


for i in l1:
    c = 0
    for j in str:
        if i == j:
            c = c +1
    print(i,c)