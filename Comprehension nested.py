#for first n natural number, find all distinct pair of number whose product is odd.

n = 10
ans = []

for i in range(1,n):
    for j in range(i+1,n):
        if i*j%2 == 1:
            ans.append((i,j))

print(ans)

ans2 = [(i,j) for i in range(1,n) for j in range(i+1,n) if i*j%2 == 1 ]

print(ans2)