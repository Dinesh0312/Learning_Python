
def sum(x):
    while x:
        s = x+sum(x-1)
        return s
    else:
        return 0

n = int (input ("Enter the  number : "))

result = sum(n)

print(result)