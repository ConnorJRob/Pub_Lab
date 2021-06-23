import unittest
from src.pub import *
from src.drink import *
from src.customer import *

class TestDrink(unittest.TestCase):

    def setUp(self):
        self.drink = Drink("Pina Colada", 4.50)

    def test_drink_has_name(self):
        self.assertEqual("Pina Colada", self.drink.name)

    def test_drink_has_price(self):
        self.assertEqual(4.50, self.drink.price)