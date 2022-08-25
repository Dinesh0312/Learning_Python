class Person:
    def __init__(self,name):
        self.name = name
    def about_me(self):
        print('Hello! I am {}'.format(self.name))
    @staticmethod
    def speak(msg):
        print(msg)

p1 = Person('Rahul')

p1.about_me()

p1.speak('A very Good Morning!!')

Person.speak('How are you doing ?')