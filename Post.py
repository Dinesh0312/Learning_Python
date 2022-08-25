list1 = [10,11,23,35,34,75,91]
list2 = [10,23,34,35,36,91,11]

for i in list1:
    if i not in list2:
        list1.append(i)
    else:
        print(i, end=" ")


