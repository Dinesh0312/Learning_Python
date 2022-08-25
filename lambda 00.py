#Lambda
#filter()
lst = [1,2,24,64,67,9,11]
even_list = list(filter((lambda n:n%2 ==0),lst))
print(even_list)

#map()
doubles = list(map(lambda n : n*2,lst))
print(doubles)

#reduce()
from functools import reduce
sum = reduce(lambda a,b : a+b,doubles)
print(sum)
