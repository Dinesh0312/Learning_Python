#function with variable length of arguments

def variable(a,b):
    print("a = {}".format(a))
    print("b = {}".format(b))

variable(2,3)


def test(*xyz):
    for i in xyz:
        print(i,end = " ")

c=input("Enter 1st value: \n")
d=input("Enter 2nd value: \n")
e=input("Enter 3st value: \n")
f=input("Enter 4nd value: \n")
test(c,d,e,f)