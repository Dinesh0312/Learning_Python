
r = 1
def sqr(x,y):
    for i in range(y):
        global r
        r = r*x
        print(r)

a = int(input("Enter the number "))
b = int(input("Enter range of the number "))
sqr(a,b)