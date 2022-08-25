#Write a Python function to sum all the numbers in a list.

lst = [8, 2, 3, 0, 7]

sum = 0
def Add():
    global sum
    for i in range(len(lst)):
        sum = sum + lst[i]
    return sum

result = Add()
print(result)



