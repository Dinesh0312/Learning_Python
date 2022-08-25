#Write a Python program to sort a given list of lists by length and value using lambda

list = [[2], [0], [1, 3], [0, 7], [9, 11], [13, 15, 17]]

def sort_sublists(list):
    result = sorted(list, key=lambda l: (len(l), l))
    return result

print(sort_sublists(list))