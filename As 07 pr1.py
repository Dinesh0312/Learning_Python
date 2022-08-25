# 1. Write a program to reverse all the words in a given sentence using function.

def reverse(str):
    str1 = ""
    for i in str:
        str1 = i + str1
    return str1


str = "Python learning"

result = reverse(str)
print(result)

#2. Write a program to print the elements of a list on even position using function

#def even_position(list1):
   # return list1[::2]

#list1 = [2,4,5,7,1,9,6]
#result = even_position(list1)
#print(result)

list1 = [2,4,5,7,1,9,6]
for i in range(0,len(list1)):  # i = 0  range (1 to 10)
    if i % 2 == 0: # 1,2,3,4,5-----10
        print('Element in Even position is {}'.format(list1[i]))
    else:
        print('Element in Odd position is {}'.format(list1[i]))

# Write a program to Remove all occurrences of a specific item from a list using function.

list1 = [1, 2, 3, 2, 4, 5, 6, 2, 7, 8, 9]

def accur(list1):
    for i in list1:
        if i == 2:
            list1.remove(i)
    print(list1)

accur(list1)

#Write a python function that prints the frequency of all the unique words. You can have a list of words or you can take data from the user.

#str1 = 'pythonassesment'

#print([{i: str1.count(i)}for i in set(str1)])

#str = 'pythonassesment'
#str = list(str)

"""def count_occur(str):
    result = dict(map(lambda i:(i, list(str).count(i)),str))
    return result

print(count_occur(str))"""

str1 = 'pythonassesment'

str1 = list(str1)

list1 = []

for i in str1:
    if i not in list1:
        list1.append(i)
print(list1)

dict = {}
for i in list1:
    c=0
    for j in str1:
        if i == j:
            c+=1
    dict[i] = c
print(dict)

# 5. Write a function that accepts a string and calculate the number of upper case letters and lower case letters. input: "This is New". output: Upper: 2, lower: 7

str = "This is New"

def letter(str):
    upper = 0
    lower = 0
    for i in str:
        if i.isupper():
            upper += 1
        if i.islower():
            lower += 1
    print("Upper : {} \nLower : {}".format(upper, lower))

letter(str)


#6. write an if condition to check if given number is even or odd using f-string (use f-sting if condition)

def math(l1):
    even = []
    odd = []
    for i in l1:
        if i%2 == 0:
            even.append(i)
        elif i%2 !=0:
            odd.append(i)
    print("Even Numbers:{}".format(even))
    print("odd numbers:{}".format(odd))

l1 = [2,5,6,7,9,8,4]
math(l1)

#7. Write a lambda function that doubles the input value.

lst = [1,2,24,64,67,9,11]
doubles = list(map(lambda n : n*2,lst))
print(doubles)

#Create a dictionary key as name and phone number as value, and print dictionary elements using f-string

def fun(dict1):
    print(f'Keys are : {dict1.keys()}, values are:{dict1.values()}')

dict1 = {'Ram': 289001,'Robert':287654}
print(fun(dict1))


# Explain module


from explain_module import Add

x = 5
y = 7

z = Add(x,y)
print(z)
