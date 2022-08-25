#Generate the running maximum, minimum value of the elements of an iterable

"""from itertools import accumulate
def running_max_product(iters):
    return accumulate(iters, max)
#List
result = running_max_product([1,3,2,7,9,8,10,11,12,14,11,12,7])
print("Running maximum value of a list:")
for i in result:
    print(i)"""


list = input("enter the string : ")

list = list.split()

def Max_word(list):
    for i in list:
        max_word = max(list,key=len)
    return max_word

result = Max_word(list)

print(result)

