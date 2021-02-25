
class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def say_hello(self):
        print(f'Hi, my name is {self.name}')


class Swimmer(Person):
    has_trunks = True

    def __init__(self, name, age, trunks_color="Blue"):
        super().__init__(name, age)
        self.trunks_color = trunks_color

    def say_hello(self):
        print(f'Hi, I am {self.name}, I love swimming')

    def takes_swim(self):
        print(f'{self.name} is enjoying a swim.')

    def change_trunks(self, new_color):
        self.trunks_color = new_color
