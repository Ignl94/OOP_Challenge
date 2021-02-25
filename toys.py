
class Toys:

    def __init__(self, name, amount):
        self.name = name
        self.amount = amount

    def inflate(self):
        print(f'{self.name} inflated.')

    def change_amount(self, new_amount):
        self.amount = new_amount
        print(f'You know have {self.amount} {self.name}.')

    def toys_squeaking(self):
        print(f'{self.name} are squeaking in the pool.')
