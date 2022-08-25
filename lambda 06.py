#Write a Python program to square and cube every number in a given list of integers using Lambda

lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

square = list(map(lambda n : n**2,lst))

print(square)

cube = list(map(lambda n : n**3,lst))

print(cube)