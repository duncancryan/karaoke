import unittest
from classes.room import Room
from classes.guest import Guest
from classes.song import Song

class TestRoom(unittest.TestCase):
    def setUp(self):
        room_01 = Room("The Party Room")
        room_02 = Room("The Date Room")

    def test_room_has_name(self):
        name = self.room_01.name
        self.assertEqual("The Party Room", name)

    def test_room_pax_starts_at_0(self):
        pax = len(self.room_01.pax)
        self.assertEqual(0, pax)

    def test_room_songs_start_at_0(self):
        songs = len(self.room_01.songs)
        self.assertEqual(0, songs)