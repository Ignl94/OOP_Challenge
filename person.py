
class Person:

    def __init__(self, name, age, fav_color):
        self.name = name
        self.age = age
        self.fav_color = fav_color

    def say_hello(self):
        print(f'Hi, my name is {self.name}')

    def change_fav_color(self, new_color):
        self.fav_color = new_color


class Swimmer(Person):
    has_trunks = True

    def __init__(self, name, age, fav_color, trunks_color="Blue"):
        super().__init__(name, age, fav_color)
        self.trunks_color = trunks_color

    def say_hello(self):
        print(f'Hi, I am {self.name}, I love swimming')

    def takes_swim(self):
        print(f'{self.name} is enjoying a swim.')

    def change_trunks(self, new_color):
        self.trunks_color = new_color


example_person = Person("Paul", 23, "Gold")
example_person.say_hello()
