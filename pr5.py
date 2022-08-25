#Python program to reverse the list

list1 = [1,3,2,4,5,6]

list2 =[]
for i in range(len(list1)-1,-1,-1):
    list2.append(list1[i])
print(list2)

list1 = [1,3,2,4,5,6,5,7,5,8]

list2 = list1.count(5)

print(list2)

for i in range(0,len(list1)):
    if list1[i] == 5:
        print(i)
