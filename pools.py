from datetime import datetime
import person
import toys

current_time = datetime.now().hour


class Pool:
    water_color = "blue"
    has_jets = True
    pool_open = None

    def __init__(self, pool_name, max_capacity):
        self.name = pool_name
        self.max_capacity = max_capacity
        self.current_capacity = 0

    def take_guest(self, *guests):
        for guest in guests:
            self.current_capacity += 1
        print(f'Current Capacity: {self.current_capacity}')

    def remove_guest(self, guest_amount):
        if isinstance(guest_amount, int):
            self.current_capacity -= guest_amount
            print(f'{guest_amount} removed.')
        else:
            print(f'Enter guest amount in integers.')

    @classmethod
    def free_swim(cls):
        if 11 <= current_time < 18:
            cls.pool_open = True
            print(True)
        else:
            cls.pool_open = False
            print(False)


pool_1 = Pool("Thompsons", 200)

Pool.free_swim()
pool_1.take_guest("Arnold", "Leah", "Jonas")
pool_1.remove_guest(1)
print(pool_1.current_capacity)
