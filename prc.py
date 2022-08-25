rstar = int(input("enter the range : "))
rend = int(input("enter the range : "))

prime = []

for i in range(rstar,rend+1):
    for j in range(2,i):
        if i%j == 0:
            break
    else:
        prime.append(i)
print(prime)