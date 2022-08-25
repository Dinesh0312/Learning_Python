#incapsulation

class Vehicle:
    def __init__(self,speed,color):
        self.__speed = speed
        self.__color = color

    def set_speed(self, value):
        self.__speed = value
    def get_speed(self):
        return self.__speed

    def set_color(self, value):
        self.__color = value
    def get_color(self):
        return self.__color

ford = Vehicle(200,'black')
ford.set_speed(400)
ford.speed = 300
print(ford.get_speed())

print(ford.get_color())