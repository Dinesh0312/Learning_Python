#lambd short list

lst = [('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]

lst.sort(key=lambda x:x[1])

print(lst)

#sort the tuples in the list based on the second items.

list =[(19542209, "New York") ,(4887871, "Alabama"), (1420491, "Hawaii"), (626299, "Vermont"), (1805832, "West Virginia"), (39865590, "California")]

list = sorted(list, key=lambda x: x[1])

print(list)

#descending order

lst1 = [100,10,10000,1,9,999,99]

lst1.sort(key=lambda x:100/x)

print(lst1)

#ascending order

lst2 = [100,10,10000,1,9,999,99]

lst2.sort(key=lambda x:x)

print(lst2)

#sort the words in the list based on their second letter from a to z

lst3=["otter", "whale", "goose", "chipmunk", "fox", "sheep", "rabbit", "marten"]

lst3 = sorted(lst3, key=lambda x: x[1])

print(lst3)