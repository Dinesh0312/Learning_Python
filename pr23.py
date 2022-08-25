#print all prime number with in a range

s_range = int(input("enter range : "))
e_range = int(input("enter range : "))

prime = []

for i in range(s_range,e_range):
    for j in range(2,i):
        if i%j == 0:
            break
    else:
        prime.append(i)
print(prime)
