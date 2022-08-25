list1 = [1,23,25,31,34,27,17]
prime = []

for i in list1:
    for j in range(2,i):
        if i%j == 0:
            break
    else:
        prime.append(i)
print(prime)

