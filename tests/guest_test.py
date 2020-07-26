import unittest
from classes.guest import Guest

class TestGuest(unittest.TestCase):
    def setUp(self):
        self.guest_01 = Guest("Frodo Baggins", 51)
        self.guest_02 = Guest("Samwise Gamgee", 36)
        self.guest_03 = Guest("Meriadoc Brandybuck", 37)
        self.guest_04 = Guest("Peregrin Took", 29)

