def function(**krwgs):
    for k,v in krwgs.items():
        print(k,v)

#function(Country='India',Capital='Delhi',Language='Hindi',Courancy='Rupees')
data = {'Country':'India','Capital':'Delhi','Language':'Hindi','Courancy':'Rupees'}

function(**data)

def fun(*arg):
    return sum(arg)

print(fun(3,6,7,12))

def fun(normal,*arg):
    print(normal)
    for i in arg:
        print(i)

data = ['fruits Market']
fruits = ['Apple','Banana','lichi','Mango']

fun(data,*fruits)

