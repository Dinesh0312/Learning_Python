#Write a Python program to create a function that takes one argument,
# and that argument will be multiplied with an unknown given number

def func_compute(n):
 return lambda x : x * n

result = func_compute(2)
print(result(15))

result = func_compute(3)
print(result(15))

result = func_compute(4)
print(result(15))

result = func_compute(5)
print(result(15))