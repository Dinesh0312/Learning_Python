#function

#Write a program to reverse all the words in a given sentence using function

def reverse(str1):
    x = ""
    for i in str1:
        x = i + x
    return x

str1 = "Apple is red"

result = reverse(str1)
print(result)


def re_verse(str):
    return str[::-1]

str1 = "Apple is red"
result = reverse(str1)
print(result)


#Write a program to print the elements of a list on even position using function

def even_position(lst1):
    lst2 = []
    for i in range(0,len(lst1)):
        if i%2 == 0:
            lst2.append(lst1[i])
    print(lst2)

lst1 = [2,3,4,6,7,9,3,234,45,56,73,2341]
result = even_position(lst1)
print(result)


#Write a function that takes a list of words and returns the length of the longest one

def longest_word(lst1):
    longest = max(lst1,key=len)
    print(longest)

lst1 = ["Apple","Pineapple","Orange"]

longest_word(lst1)

#write an if condition to check if given number is even or odd using f-string (use f-sting if condition)

def fun(lst):
    even = []
    odd = []
    for i in lst:
        if i%2 == 0:
            even.append(i)
        else:
            odd.append(i)
    print(f'Even Numbers:{even}')
    print(f'Odd Numbers:{odd}')


lst = [2,3,4,6,7,9,3,234,45,56,73,2341]
f = fun(lst)
print(f)

#create a dictionary key as name and phone number as value, and print dictionary elements using f-string

def fun(dict1):
    print(f'Keys are : {dict1.keys()}, values are:{dict1.values()}')

dict1 = {'Ram': 289001,'Robert':287654}
print(fun(dict1))

#Explain casting using online complier.

x = 1.0
print(int(x))

y = 12
print(float(y))

z = 14
print(str(z))

x = 1
print(type(x))

#7 Explain the modules by writing the programs.

from calculator import Add

z = Add(5,6)
print(z)

