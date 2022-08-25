#1. Write a function in python to count the number of lines in a text file 'STORY.TXT'
# which is starting with an alphabet 'A'.

def countlines():
    file = open('STORY.TXT','r')
    lines = file.readlines()
    count = 0
    for word in lines:
        if word[0]=="A" or word[0]=="a":
            count = count+1
    print("Total lines", count)
    file.close()

countlines()

#Write a method/function DISPLAYWORDS() in python to read lines from a text file STORY.TXT and display those words ,which is less than 4 characters.

def displaywords():
    file = open('STORY.TXT', 'r')
    line = file.read()
    word = line.split()
    for w in word:
        if len(w) < 4:
            print(w)
    file.close()

displaywords()

#3. Write a function in python to count the number of lowercase alphabets present in a text file "STORY.TXT".

def lowercount():
    f = open("STORY.TXT", "r")
    lines = f.read()
    count = 0
    for letter in lines:
        if letter.islower():
            count = count + 1
    print("Total lower aplhabets", count)

lowercount()


#4. Define a function to add all the arguments, use arguments positional, keyword and *args.


def fun(name, age, *num, location="Bangalore"):
    sum = 0
    for i in num:
        sum = sum + i
    print(f'My name is {name}. I am {age} years old and salary is {sum} thousand at location {location}')

fun("James", 33, 15, 10, 30)

#5. What is oops concept and explain with sample programs in class ?

"""
OOP's concepts like, Classes,Encapsulation,Polymorphism, Inheritance etc. 
in Python are makes it as a object oriented programming language.

Object have two properties-
1.	Attributes – (Variables) -:
    i.	Instance Variable 
    ii.	Class(static) Variable
2.	Methods – (function)-:
    i.	Instance Method 
    ii.	Class Method
    iii.Static Method

Classes – It is a blueprint/Design of an object .
"""
class Laptop:

    def __init__(self,CPU,RAM):
        self.CPU = CPU
        self.RAM = RAM

    def config(self):
        print(f"Config is - CPU {self.CPU} , RAM {self.RAM}")

Lap1 = Laptop('i3','8gb')
Lap2 = Laptop('i7','16gb')

Lap1.config()
Lap2.config()

