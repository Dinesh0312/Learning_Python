#Paramerterized

@preetify
def print_name(name):
    print(name)

@preetify
def print_city(city):
    print(city)

print_name('Varun')
print_city('Lucknow')


def preetify(func):

    def wrapper(text):
        print('*'*text)
        func(text)
        print('*'*text)
    return wrapper