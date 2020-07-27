import unittest
from classes.drink import Drink

class TestDrink(unittest.TestCase):
    def setUp(self):
        self.drink_01 = Drink("Gaffer's Home Brew", 5)
        self.drink_02 = Drink("Dry Martini", 2)
        self.drink_03 = Drink("Margarita", 2)
        self.drink_04 = Drink("Manhattan", 2)
        self.drink_05 = Drink("Sazerac", 3)
        self.drink_06 = Drink("Highball", 1)

    def test_drink_has_name(self):
        name = self.drink_01.name
        self.assertEqual("Gaffer's Home Brew", name)

    def test_drink_has_alcohol_level(self):
        abv = self.drink_02.alcohol
        self.assertEqual(2, abv)
