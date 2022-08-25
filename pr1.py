
#Create 2 list with number and string combinations. Use for loop to create a new list with common value

list1 = [3, 6,'B', 4, 'a',9,'z','d']
list2 = ['x',2,3,'d',9]

list3 = []

for i in list1:
    for j in list2:
        if (i == j):
            list3.append(i)
print(list3)
