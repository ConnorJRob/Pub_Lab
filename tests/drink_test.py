import unittest
from src.pub import *
from src.drink import *
from src.customer import *

class TestDrink(unittest.TestCase):

    def setUp(self):
        # The test is set up with the below Drink class which will be the case at the beginning of every test
        self.drink = Drink("Pina Colada", 4.50)

    def test_drink_has_name(self):
        #This test checks that given the Drink Class created above, the drink.name property has been correctly setup matching "Pina Colada"
        self.assertEqual("Pina Colada", self.drink.name)

        #This test checks that given the Drink Class created above, the drink.price property has been correctly setup matching 4.50
    def test_drink_has_price(self):
        self.assertEqual(4.50, self.drink.price)