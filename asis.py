
str = "aaaggggjjjjooo"

str = list(str)


l = [{ i: str.count(i)}for i in set(str)]

print(l)

str = "aaaggggjjjjooo"

def my_fun(n):
    return len(n)

x = map(my_fun,("aaaggggjjjjooo"))

