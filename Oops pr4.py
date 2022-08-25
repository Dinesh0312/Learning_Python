class Vehicle:

    def __init__(self,milage,cost):
        self.milage = milage
        self.cost = cost

    def show_vehicle_details(self):
        print("I am a Vehicle")
        print("Vehicle milage is ",self.milage)
        print("Vehicle cost is ",self.cost,"\n")

class Car(Vehicle):
    def __init__(self,milage,cost,tyres,hp):
        super().__init__(milage,cost)
        self.tyres = tyres
        self.hp = hp

    def show_car_details(self):
        print("I am a car")
        print("Car tyres is ",self.tyres)
        print("Car Hp is ",self.hp)

v1= Vehicle(25,36000)
v1.show_vehicle_details()

c1 = Car(20,30000,4,250)
c1.show_car_details()

