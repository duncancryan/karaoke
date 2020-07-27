import unittest
from classes.guest import Guest
from classes.room import Room
from classes.song import Song
from classes.drink import Drink

class TestGuest(unittest.TestCase):
    def setUp(self):
        self.room_01 = Room("The Party Room", 4, 5.00)
        self.room_02 = Room("The Date Room", 2, 10.00)

        self.drink_01 = Drink("Gaffer's Home Brew", 5, 1.20)
        self.drink_02 = Drink("Dry Martini", 2, 3.40)
        self.drink_03 = Drink("Margarita", 2, 3.40)
        self.drink_04 = Drink("Manhattan", 2, 3.40)
        self.drink_05 = Drink("Sazerac", 3, 4.25)
        self.drink_06 = Drink("Highball", 1, 2.60)
        
        self.song_01 = Song("Come on Eileen", "Dexys Midnight Runners")
        self.song_02 = Song("Mr Blue Sky", "ELO")
        self.song_03 = Song("Bat out of Hell", "Meatloaf")
        self.song_04 = Song("You're so Vain", "Carly Simon")
        self.song_05 = Song("Tubthumping", "Chumbawamba")
        self.song_06 = Song("Accidentally in Love", "Counting Crows")
        
        self.guest_01 = Guest("Frodo Baggins", 51, 30.50, self.song_04, self.drink_06)
        self.guest_02 = Guest("Samwise Gamgee", 36, 10.75, self.song_03, self.drink_01)
        self.guest_03 = Guest("Meriadoc Brandybuck", 37, 23.60, self.song_01, self.drink_05)
        self.guest_04 = Guest("Peregrin Took", 29, 17.85, self.song_05, self.drink_03)

    def test_guest_has_name(self):
        name = self.guest_01.name
        self.assertEqual("Frodo Baggins", name)
    
    def test_guest_has_age(self):
        age = self.guest_01.age
        self.assertEqual(51, age)

    def test_guest_has_wallet(self):
        wallet = round(self.guest_02.wallet, 2)
        self.assertEqual(10.75, wallet)

    def test_wallet_can_decrease(self):
        self.guest_04.decrease_wallet(4.85)
        self.assertEqual(round(self.guest_04.wallet, 2), 13.00)

    def test_guest_can_pay_entry(self):
        self.guest_03.pay_entry(self.room_01)
        self.assertEqual(round(self.guest_03.wallet, 2), 18.60)
        self.assertEqual(round(self.room_01.bill, 2), 5.00)

    def test_guest_has_favourite_song(self):
        fav_song = self.guest_01.fav_song
        self.assertEqual(self.song_04, fav_song)

    def test_reacts_to_fav_song(self):
        reaction = self.guest_03.react_to_song(self.song_01)
        self.assertEqual("Wahey!", reaction)

    def test_guest_has_favourite_drink(self):
        fav = self.guest_02.fav_drink
        self.assertEqual(self.drink_01, fav)

    def test_guest_can_afford_drink(self):
        pass
