#Find out the duplicate from the list and also get the count of each duplicate.
l1 = [1,3,4,1,5,6,6,7,8,8,8,9]

l2 = []

for i in l1:
    if i not in l2:
        l2.append(i)
print(l2)


for i in l2:
    c = 0
    for j in l1:
        if j == i:
            c = c+1
    print(f"value {i} , count {c}")