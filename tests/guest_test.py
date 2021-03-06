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
        self.room_01.add_song(self.song_01)
        reaction = self.guest_03.react_to_song(self.room_01)
        self.assertEqual("Wahey!", reaction)

    def test_guest_has_favourite_drink(self):
        fav = self.guest_02.fav_drink
        self.assertEqual(self.drink_01, fav)

    def test_guest_can_afford_drink_false(self):
        self.guest_02.pay_entry(self.room_02)
        result = self.guest_02.can_afford(self.drink_01)
        self.assertEqual(False, result)

    def test_guest_can_afford_drink_true(self):
        self.guest_01.pay_entry(self.room_02)
        result = self.guest_01.can_afford(self.drink_01)
        self.assertEqual(True, result)

    def test_guest_singing_prowess_starts_at_0(self):
        confidence = self.guest_02.singing_prowess
        self.assertEqual(0, confidence)

    def test_prowess_can_increase(self):
        self.guest_02.increase_prowess(5)
        self.assertEqual(5, self.guest_02.singing_prowess)
        
    def test_customer_can_buy_drink(self):
        self.guest_03.pay_entry(self.room_01)
        self.guest_03.buy_drink(self.drink_05, self.room_01)
        self.assertEqual(14.35, round(self.guest_03.wallet, 2))
        self.assertEqual(9.25, round(self.room_01.bill, 2))
        self.assertEqual(3, self.guest_03.singing_prowess)
