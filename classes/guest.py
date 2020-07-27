class Guest:
    def __init__(self, name, age, wallet, fav_song):
        self.name = name
        self.age = age
        self.wallet = wallet
        self.fav_song = fav_song

    def decrease_wallet(self, amount):
        self.wallet -= amount

    def pay_entry(self, room):
        self.decrease_wallet(room.fee)
        room.increase_bill(room.fee)

    def react_to_song(self, song):
        if song == self.fav_song:
            return "Wahey!"

            # or...?

    # def react_to_song(self, room):
    #     if self.fav_song in room.songs:
    #         return "Wahey!"

    
