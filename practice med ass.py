# Count the lengthy and short name count from user input list

lst = []

x = int(input("How many name would you like to enter : "))

for i in range(x):
    lst.append(input("Enter the name : "))


def func(lst):
    lengthy_name = 0
    short_name = 0
    for i in lst:
        if len(i) > 5:
            lengthy_name += 1
        else:
            short_name += 1
    return lengthy_name, short_name

l, s = func(lst)

z = "lengthy_name count : {} and short_name count : {}"

print(z.format(l, s))


