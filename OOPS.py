
class Computer:

    def __init__(self,CPU,RAM):
        self.CPU = CPU
        self.RAM = RAM

    def config(self):
        print("Config is ",self.CPU,self.RAM)

com1 = Computer('i3','16gb')
com2= Computer('Ryzen 3','8gb')

com1.config()
com2.config()

