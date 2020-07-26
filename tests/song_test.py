import unittest
from classes.song import Song

class TestSong(unittest.TestCase):
    def setUp(self):
        self.song_01 = Song("Come on Eileen", "Dexys Midnight Runners")
        self.song_02 = Song("Mr Blue Sky", "ELO")
        self.song_03 = Song("Bat out of Hell", "Meatloaf")
        self.song_04 = Song("You're so Vain", "Carly Simon")
        self.song_05 = Song("Tubthumping", "Chumbawamba")
        self.song_06 = Song("Accidentally in Love, Counting Crows")

    def test_song_has_name(self):
        name = self.song_01.name
        self.assertEqual("Come on Eileen", name)

    def test_song_has_artist(self):
        artist = self.song_02.artist
        self.assertEqual("ELO", artist)