#Closure
def Outer_func():
    msg = 'Hi'
    def Inner_func():
        print(msg)
    return Inner_func

my_func = Outer_func()
print(my_func.__name__)
my_func()

def Outer_func(msg):
    message = msg
    def Inner_func():
        print(message)
    return Inner_func

hi_func = Outer_func('Hi')
hello_func = Outer_func('Hello')
hi_func()
hello_func()

