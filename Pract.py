l1= [10,20,30,60]
l2= [20,50,90,10]

#o/p = [10,20]

print(set(l1).intersection(l2))

for i in l1:
    if i not in l2:
        l1.append(i)
    else:
        print(i,end='')

def common(l1,l2):
    c = [i for i in l1 if i in l2]
    return c
d=common(l1,l2)
print(d)




