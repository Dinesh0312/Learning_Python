#Consider the following function that sums up two numbers.

def sum(a, b):
    return a + b

print(sum(2, 6))

def add(*args):
    result = 0
    for i in args:
        result += i
    return result

print(add(3, 5))

#In the following function, the option is a keyword argument (it has a default value).

def addition(a, b, *args, option=True):
   result = 0
   if option:
      for i in args:
        result += i
      return a + b + result
   else:
      return result

print(addition(1,4,5,6,7))

print(addition(1,4,5,6,7, option=False))

#We can use both *args and **kwargs in a function but *args must be put before **kwargs.

def arg_printer(a, b,*args, option=True, **kwargs):
   print(a, b)
   print(args)
   print(option)
   print(kwargs)

arg_printer(1, 4, 5, 6, param1=5, param2=6)


#We can pack and unpack variables using *args and **kwargs.

def arg_printer(*args):
   print(args)

lst = [1,4,5]
arg_printer(lst)
arg_printer(*lst)

lst = [1,4,5]
tpl = ('a','b',4)
arg_printer(*lst, *tpl, 5, 6)



def arg_printer(**kwargs):
   print(kwargs)

dct = {'param1':5, 'param2':8}
arg_printer(**dct)

dct = {'param1':5, 'param2':8}
arg_printer(param3=9, **dct)



