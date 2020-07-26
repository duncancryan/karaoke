import unittest
from classes.guest import Guest

class TestGuest(unittest.TestCase):
    def setUp(self):
        self.guest_01 = Guest("Frodo Baggins", 51, 30.50)
        self.guest_02 = Guest("Samwise Gamgee", 36, 10.75)
        self.guest_03 = Guest("Meriadoc Brandybuck", 37, 23.60)
        self.guest_04 = Guest("Peregrin Took", 29, 17.85)

    def test_guest_has_name(self):
        name = self.guest_01.name
        self.assertEqual("Frodo Baggins", name)
    
    def test_guest_has_age(self):
        age = self.guest_01.age
        self.assertEqual(51, age)

    def test_guest_has_wallet(self):
        wallet = round(self.guest_02.wallet, 2)
        self.assertEqual(10.75, wallet)

