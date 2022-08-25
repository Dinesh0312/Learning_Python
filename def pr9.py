#Write a Python function that takes a list and returns a new list with unique elements of the first list

list = [1,2,3,3,3,3,4,5,6,5,1,2]

list1 = []

def unique_elements(list):
    for i in list:
        if i not in list1:
            list1.append(i)
    return list1

result = unique_elements(list)

print(result)