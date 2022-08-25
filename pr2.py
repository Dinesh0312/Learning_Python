n = 4
for i in range(n):
    for j in range(n-i):
        print("#",end=" ")
    print()


n=5
for i in range(n):
    for j in range(1,n-i):
        print("",end="")
    for k in range(0,i+1):
        print("#",end=" ")
    print()

