#Write a Python program to create a shallow copy of a given list. Use copy.copy
import copy
nums_x = [1, [2, 3, 4]]
print("Original list: ", nums_x)
nums_y = copy.copy(nums_x)
print("Copy of the said list:")
print(nums_y)
print("Change the value of an element of the original list:")
nums_x[1][1] = 10
print(nums_x)
print("Second list:")
print(nums_y)
#Write a Python program to create a deep copy of a given list. Use copy.copy
import copy
nums_x = [1, [2, 3, 4]]
print("\nOriginal list: ", nums_x)
nums_y = copy.deepcopy(nums_x)
print("Deep copy of the said list:")
print(nums_y)
print("Change the value of an element of the original list:")
nums_x[1][1] = 10
print(nums_x)
print("Copy of the second list (Deep copy):")
print(nums_y)

#Write a Python program to create a shallow copy of a given dictionary. Use copy.copy

import copy
nums_x = {"a":1, "b":2, 'cc':{"c":3}}
print("\nOriginal dictionary: ", nums_x)
nums_y = copy.copy(nums_x)
print("Copy of the said list:")
print(nums_y)
print("Change the value of an element of the original dictionary:")
nums_x["cc"]["c"] = 10
print(nums_x)
print("Second dictionary:")
print(nums_y)


#Write a Python program to create a deep copy of a given dictionary. Use copy.copy

import copy
nums_x = {"a":1, "b":2, 'cc':{"c":3}}
print("\nOriginal dictionary: ", nums_x)
nums_y = copy.deepcopy(nums_x)
print("Deep copy of the said list:")
print(nums_y)
print("Change the value of an element of the original dictionary:")
nums_x["cc"]["c"] = 10
print(nums_x)
print("Second dictionary (Deep copy):")
print(nums_y)