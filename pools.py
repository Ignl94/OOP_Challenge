from datetime import datetime
from person import Swimmer
from toys import Toys

current_time = datetime.now().hour


class Pool:
    water_color = "blue"
    has_jets = True
    pool_open = None

    def __init__(self, pool_name, max_capacity=50):
        self.name = pool_name
        self.max_capacity = max_capacity
        self.current_capacity = 0
        self.guest_list = []

    def take_guest(self, *guests):
        for guest in guests:
            self.current_capacity += 1
            self.guest_list.append(guest)
        print(f'Current Capacity: {self.current_capacity}')

    def remove_guest(self, guest):
        if guest in self.guest_list:
            self.guest_list.remove(guest)
            self.current_capacity -= 1
        else:
            print("Person not on list.")

    def pool_party(self):
        guest_found = False
        list_check = input("What is your name? ")
        for guest in self.guest_list:
            if guest.name == list_check:
                guest_found = True
                print("Welcome to the party!")
                guest.say_hello()
                guest.takes_swim()
                Toys.inflate()
                floties.toys_squeaking()
        if guest_found == False:
            print("Your not on the list.")

    @classmethod
    def free_swim(cls):
        if 11 <= current_time < 18:
            cls.pool_open = True
            print(True)
        else:
            cls.pool_open = False
            print(False)


# -------------------  Instantiations ---------------------
pool_1 = Pool("Thompson's", 200)
# --------------------------------------------------
anita = Swimmer("Anita", 23, "Blue", "Yellow")
bryan = Swimmer("Bryan", 20, "Orange", "Green")
claudia = Swimmer("Claudia", 20, "Purple", "Gold")
jose = Swimmer("Jose", 22, "Blue", "Blue")
# --------------------------------------------------
balls = Toys("Pool Balls", 2)
floties = Toys("Floties", 7)
# -----------------------------------------------
Pool.free_swim()
pool_1.take_guest(anita, bryan, claudia, jose)
print(pool_1.guest_list)
pool_1.pool_party()
