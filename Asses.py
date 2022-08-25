
#Write Example of class

class Laptop:
    def __init__(self,CPU,RAM):
        self.CPU = CPU
        self.RAM = RAM

    def config(self):
        print("Config of Laptop is",self.RAM,self.CPU)

lap1 = Laptop('i3','8gb')
lap2 = Laptop('i7','16gb')

lap1.config()
lap2.config()

#Write a Example of closure

def Outer_func():
    msg = 'Hi'
    def Inner_func():
        print(msg)
    return Inner_func

My_func = Outer_func()
print(My_func.__name__)
My_func()

#Write a Example of decorator

def div(a,b):
    print(a/b)

def smart_div(func):
    def inner(a,b):
        if a<b:
            a,b = b,a
        return func(a,b)
    return inner

div = smart_div(div)
div(2,6)

#Write a Example of inheritance

class A:
    def feature1(self):
        print("Feature 1 is working")
    def feature2(self):
        print("Feature 2 is working")

class B:
    def feature3(self):
        print("Feature 3 is working")
    def feature4(self):
        print("Feature 4 is working")

class C(A,B):
    def feature5(self):
        print("Feature 5 is working")

c1 = C()
c1.feature1()
c1.feature3()
c1.feature5()

#Write a Example of encapsulation

class Car:
    def __init__(self,speed,color):
        self.__speed = speed
        self.__color = color

    def set_speed(self,value):
        self.__speed = value
    def get_speed(self):
        return self.__speed

    def set_color(self,value):
        self.__color = value
    def get_color(self):
        return self.__color

ford = Car(500,'Black')
ford.set_speed(800)

print(ford.get_speed())
print(ford.get_color())

#Example of staticmethod and classmethod

class Student:
    School = 'Dewan Public School'
    def __init__(self,m1,m2,m3):
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3
    def avg(self):
        return (self.m1+self.m2+self.m3)/3
    @classmethod
    def get_school(cls):
        return cls.School
    @staticmethod
    def Info():
        print("This is a CBSE School")

s1 = Student(45,56,78)
s2 = Student(67,54,34)

print(s1.avg())
print(s2.avg())

print(Student.School)

Student.Info()



print("how are you")