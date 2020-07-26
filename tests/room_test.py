import unittest
from classes.room import Room
from classes.guest import Guest
from classes.song import Song

class TestRoom(unittest.TestCase):
    def setUp(self):
        self.room_01 = Room("The Party Room")
        self.room_02 = Room("The Date Room")
        
        self.guest_01 = Guest("Frodo Baggins", 51)
        self.guest_02 = Guest("Samwise Gamgee", 36)
        self.guest_03 = Guest("Meriadoc Brandybuck", 37)
        self.guest_04 = Guest("Peregrin Took", 29)

        self.song_01 = Song("Come on Eileen", "Dexys Midnight Runners")
        self.song_02 = Song("Mr Blue Sky", "ELO")
        self.song_03 = Song("Bat out of Hell", "Meatloaf")
        self.song_04 = Song("You're so Vain", "Carly Simon")
        self.song_05 = Song("Tubthumping", "Chumbawamba")
        self.song_06 = Song("Accidentally in Love", "Counting Crows")

    def test_room_has_name(self):
        name = self.room_01.name
        self.assertEqual("The Party Room", name)

    def test_room_pax_starts_at_0(self):
        pax = len(self.room_01.guests)
        self.assertEqual(0, pax)

    def test_room_songs_start_at_0(self):
        songs = len(self.room_01.songs)
        self.assertEqual(0, songs)
    
    def test_room_can_check_out_customer(self):
        self.room_02.check_in_guest(self.guest_02)
        self.assertEqual(1, len(self.room_02.guests))

    def test_room_can_check_out_guest(self):
        self.room_02.check_in_guest(self.guest_02)
        self.room_02.check_out_guest(self.guest_02)
        self.assertEqual(0, len(self.room_02.guests))

