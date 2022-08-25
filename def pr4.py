#Write a Python function to multiply all the numbers in a list.

lst = [8, 2, 3,-1, 7]

def multi(lst):
    m = 1
    for i in lst:
        m = m*i
    return m

result = multi(lst)

print(result)