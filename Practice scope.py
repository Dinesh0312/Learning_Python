
x = 5
def func():
    x = 10
    z = globals()['x']
    globals()['x'] = 8
    print("inside",x)

func()
print("outside",x)

