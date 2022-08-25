
class Employee:

    def __init__(self,name,age,salary,gender):
        self.name = name
        self.age = age
        self.salary = salary
        self.gender = gender

    def show_employee_details(self):
        print(f"Name of employee is {self.name}\nAge of employee is {self.age}\nSalary of employee is {self.salary}\nGender of employee is {self.gender}\n")



Emp1 = Employee('Rahul',28,60000,'Male')
Emp2 = Employee('Soniya',25,40000,'Female')

Emp1.show_employee_details()
Emp2.show_employee_details()


