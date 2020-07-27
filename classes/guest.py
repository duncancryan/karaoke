class Guest:
    def __init__(self, name, age, wallet, fav_song, fav_drink):
        self.name = name
        self.age = age
        self.wallet = wallet
        self.fav_song = fav_song
        self.fav_drink = fav_drink
        self.singing_prowess = 0

    def decrease_wallet(self, amount):
        self.wallet -= amount

    def pay_entry(self, room):
        self.decrease_wallet(room.fee)
        room.increase_bill(room.fee)

    # def react_to_song(self, song):
    #     if song == self.fav_song:
    #         return "Wahey!"

            # or...?

    def react_to_song(self, room):
        if self.fav_song in room.songs:
            return "Wahey!"

    
    def can_afford(self, drink):
        if self.wallet >= drink.price:
            return True
        return False

    def increase_prowess(self, amount):
        self.singing_prowess += amount

    def buy_drink(self, drink, room):
        if self.can_afford(drink):
            self.decrease_wallet(drink.price)
            room.increase_bill(drink.price)
            self.increase_prowess(drink.alcohol)
