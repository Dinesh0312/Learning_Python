
class Pycham:
    def execute(self):
        print("Compiling")
        print("Running")

class MyEditor:

    def execute(self):
        print("spell check")
        print("convenctional check")
        print("Compiling")
        print("Running")

class Laptop:
    def code(self,ide):
        ide.execute()

#ide = Pycham()
lap1 = Laptop()

#lap1.code(ide)

ide = MyEditor()

lap1.code(ide)