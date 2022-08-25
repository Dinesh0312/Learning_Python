#Inheritence

class Parent:
    def get_name(self,name):
        self.name = name
    def show_name(self):
        return self.name

class Child(Parent):
    def get_age(self,age):
        self.age = age
    def show_age(self):
        return self.age

class Grand_child(Child):
    def get_gender(self,gender):
        self.gender = gender
    def show_gender(self):
        return self.gender

gc = Grand_child()
gc.get_name("Rohan")
gc.get_age(24)
gc.get_gender("Male")


print(gc.show_name())
print(gc.show_age())
print(gc.show_gender())

