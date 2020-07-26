class Room:
    def __init__(self, name, limit, fee):
        self.name = name
        self.limit = limit
        self.fee = fee
        self.guests = []
        self.songs = []
        self.bill = 0.00

    def check_in_guest(self, guest):
        if len(self.guests) < self.limit:
            self.guests.append(guest)

    def check_out_guest(self, guest):
        self.guests.remove(guest)

    def empty_room(self):
        self.guests.clear()

    def add_song(self, song):
        self.songs.append(song)
