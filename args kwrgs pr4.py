
def fun(*args):
    c=0
    for i in args:
        c = c + i
    print(c)

fun(2,3,4,5,6,7)


def fun(**kargs):
    for k,v in kargs.items():
        print(k,v)

fun(Name='Rahul',age=24,Location='Delhi')


def data(normal,*args,**kargs):
    print(normal)
    for item in args:
        print(item)

    for k,v in kargs.items():
        print(k,v)

normal = 'india'
file = ['apple','mango','orange']
schl  = {'name':'dma','location':'meerut','board':'cbse'}

data(normal,*file,**schl)
