#create two list with number and string and print the common items of both list in list 3

l1=[3,6,"b",4,"a",9,"z","d"]
l2=["x",2,3,"d",9]

print(set(l1).intersection(l2))



for i in l1:
    for j in l2:
        if i == j:
            print(j,end=" ")
