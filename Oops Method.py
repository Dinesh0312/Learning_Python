class Student:
    School = 'Dewan Public School'
    def __init__(self,m1,m2,m3):
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3
    def avg(self):
        return (self.m1+self.m2+self.m3)/3
    def get_m1(self):
        return self.m1
    def set_m1(self,value):
        self.m1 = value
    @classmethod
    def get_school(cls):
        return cls.School
    @staticmethod
    def info():
        print("This is the class of students s1 and s2")

s1 = Student(45,58,78)
s2 = Student(67,72,56)

print(s1.avg())
print(s2.avg())
print(s1.m1)
print(s1.get_m1())

s1.set_m1(88)
print(s1.avg())

print(s1.m1)

print(Student.get_school())

Student.info()