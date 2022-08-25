

class Car:
    
    Wheels = 4

    def __init__(self):
        self.mil = '10'
        self.name = 'BMW'


c1 = Car()
c2 = Car()

c2.name = 'Audi'
Car.Wheels = 5

print(c1.mil,c1.name,c1.Wheels)
print(c2.mil,c2.name,c2.Wheels)