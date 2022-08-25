l1 =['a', 'b', 'c', 'c', 'c', 'c', 'c', 'd', 'e', 'e', 'g', 'g']
l2 =['a', 'b', 'c', 'd', 'e', 'g']

dict = {}
for i in l2:
    dict[i] = l1.count(i)
print(dict)