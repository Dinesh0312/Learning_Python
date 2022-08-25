str1 = ' Rockstar of the Galaxy '

str1 = str1.split()

print(str1)

for i in str1:
    c = 0
    for j in i:
        c = c + 1
    print(i, c)

for i in str1:
    print(i, len(i))

for i in str1:
    if i == str1[-1]:
        print(i, len(i))
