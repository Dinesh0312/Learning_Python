#closure

class Student:
    def __init__(self,name,rollno):
        self.name = name
        self.rollno = rollno
        self.laptop = self.Laptop()
    def show(self):
        print(self.name,self.rollno)
        self.laptop.show()
    class Laptop:
        def __init__(self):
            self.brand = 'HP'
            self.cpu = 'i5'
            self.ram = '8gb'
        def show(self):
            print(self.brand,self.ram,self.cpu)

s1 = Student('Navin',22)
s2 = Student('Aman',25)
s2.show()


