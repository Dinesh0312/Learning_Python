#1) Find out the duplicate from the list and also get the count of each duplicate.(Num and Alpa)
#[p,3,4,1,A,6,A,B,8,8,c,9,D,E, E, AA, aa, aa]

lst = ['p',3,4,1,'A',6,'A','B',8,8,'c',9,'D','E', 'E', 'AA', 'aa', 'aa']

list1 = []
for i in lst:
    if i not in list1:
        list1.append(i)
print(list1)

dict = {}

for i in list1:
    dict[i] = lst.count(i)
print(dict)

#2.1)  Compare the first and last name and print the uncommon alphabets in your name