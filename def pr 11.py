#Write a Python program to print the even numbers from a given list

list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

def even(list):
    list1 = []
    for i in list:
        if i%2 == 0:
            list1.append(i)
    return list1

result = even(list)

print(result)