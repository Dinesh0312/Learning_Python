
class Computer:
    def __init__(self):
        self.name = 'Dinesh'
        self.age = '25'
    #def update(self):
       # self.age = '30'
    def compare(self,other):
        if self.age == other.age:
            return True
        else:
            return False

c1 = Computer()
c2 = Computer()
c1.name = 'Rahul'
c1.age = '25'
if c1.compare(c2):
    print("They are same")
else:
    print("They are not same")

#c1.update()
print(c1.name)
print(c1.age)