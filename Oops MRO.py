
class A:

    def __init__(self):
        print("In A Init")

    def feature1(self):
        print("feature 1 is working")

    def feature2(self):
        print("feature 2 is working")

#class B(A):
class B:

    def __init__(self):
#        super().__init__()
        print("In B Init")

    def feature3(self):
        print("feature 3 is working")

    def feature4(self):
        print("feature 4 is working")

class C(A,B):

    def __init__(self):
        super().__init__()
        print("In C Init")

    def feat(self):
        super().feature2()

a1 = C()
a1.feat()