#Create an iterator from several iterators

from itertools import chain
def chain_func(l1,l2,l3):
    return chain(l1,l2,l3)
#List
result = chain_func([1,2,3], ['a','b','c','d'], [4,5,6,7,8,9])
print("Type of the new iterator:")
print(type(result))
print("Elements of the new iterator:")
for i in result:
    print(i)