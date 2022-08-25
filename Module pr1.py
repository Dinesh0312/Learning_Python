#Select a random element from a list, set, dictionary and a file from a directory

import random
import os

print("Select a random element from a list:")
elements = [1,2,3,4,5,6]

print(random.choice(elements))
print(random.choice(elements))

print("\nSelect a random element from a set:")
elements = set([1, 2, 3, 4, 5, 6])

print(random.choice(tuple(elements)))
print(random.choice(tuple(elements)))

print("\nSelect a random value from a dictionary:")

elements = {"a": 1, "b": 2, "c": 3, "d": 4, "e": 5}

key = random.choice(list(elements))
print(elements[key])
key = random.choice(list(elements))
print(elements[key])

print("\nSelect a random file from a directory.:")

print(random.choice(os.listdir("/")))