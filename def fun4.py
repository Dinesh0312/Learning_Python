#factorial

def fac(n):
    f = 1
    for i in range(1,n+1):
        f = f*i
    return f

x = int(input("Enter the number : "))

result = fac(x)

print(result)