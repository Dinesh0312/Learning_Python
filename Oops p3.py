class Vehicle:

    def __init__(self,milage,cost):
        self.milage = milage
        self.cost = cost

    def show_vehicle_details(self):
        print("I am a Vehicle")
        print("Vehicle milage is ",self.milage)
        print("Vehicle cost is ",self.cost,"\n")

class Car(Vehicle):
    def show_car_details(self):
        print("I am a Car")
        print("Car milage is ",self.milage)
        print("Car cost is ",self.cost)

v1 = Vehicle(40,80000)
v1.show_vehicle_details()

c1 = Car(35,700000)
c1.show_car_details()


