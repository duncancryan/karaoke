import unittest
from classes.room import Room
from classes.guest import Guest
from classes.song import Song
from classes.drink import Drink

class TestRoom(unittest.TestCase):
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

    def test_room_has_name(self):
        name = self.room_01.name
        self.assertEqual("The Party Room", name)

    def test_room_pax_starts_at_0(self):
        pax = len(self.room_01.guests)
        self.assertEqual(0, pax)

    def test_room_songs_start_at_0(self):
        songs = len(self.room_01.songs)
        self.assertEqual(0, songs)

    def test_room_has_guest_limit(self):
        limit = self.room_02.limit
        self.assertEqual(2, limit)

    def test_room_bill_starts_at_0(self):
        self.assertEqual(0.00, self.room_01.bill)
    
    def test_room_can_check_out_customer(self):
        self.room_02.check_in_guest(self.guest_02)
        self.assertEqual(1, len(self.room_02.guests))
    
    def test_room_has_entry_fee(self):
        fee = self.room_01.fee
        self.assertEqual(5, fee)

    def test_room_can_check_out_guest(self):
        self.room_02.check_in_guest(self.guest_02)
        self.room_02.check_out_guest(self.guest_02)
        self.assertEqual(0, len(self.room_02.guests))

    def test_empty_room(self):
        self.room_02.check_in_guest(self.guest_02)
        self.room_02.check_in_guest(self.guest_04)
        self.room_02.empty_room()
        self.assertEqual(0, len(self.room_02.guests))

    def test_song_can_be_added_to_room(self):
        self.room_02.add_song(self.song_02)
        self.assertEqual(1, len(self.room_02.songs))

    def test_full_room_will_not_take_guest(self):
        self.room_02.check_in_guest(self.guest_03)
        self.room_02.check_in_guest(self.guest_04)
        self.room_02.check_in_guest(self.guest_02)
        self.assertEqual(2, len(self.room_02.guests))

    def test_bill_can_increase(self):
        self.room_01.increase_bill(3.75)
        self.assertEqual(round(self.room_01.bill, 2), 3.75)


