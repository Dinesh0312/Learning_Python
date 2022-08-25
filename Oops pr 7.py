class employee:
    def __init__(self,first,last,pay):
        self.fname = first
        self.lname = last
        self.pay = pay
        self.email = first + '.' + last + '@test.com'
    def fulname(self):
        return self.fname + ' ' + self.lname

emp_1 = employee('Tanishq','Singh',100)
emp_2 = employee('Kavya','Singh',200)

print(emp_2.email)
print(emp_1.fulname())
print(employee.fulname(emp_2))

