class Guest:
    def __init__(self, name, age, wallet):
        self.name = name
        self.age = age
        self.wallet = wallet

    def decrease_wallet(self, amount):
        self.wallet -= amount

    def pay_entry(self, room):
        self.decrease_wallet(room.fee)
        room.increase_bill(room.fee)
        
