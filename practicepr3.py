#Write a Python program to create a shallow copy of a given list. Use copy.copy

import copy

num_x = [1,[1,2,3]]

print("Original list :",num_x)

num_y = copy.deepcopy(num_x)
print(num_y)

num_y[1][0] = 10
print(num_y)
print(num_x)