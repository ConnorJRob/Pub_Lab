import unittest
from src.drink import *
from src.customer import *

class TestCustomer(unittest.TestCase):

    def setUp(self):
        self.customer = Customer("Princess", 20.00)

    def test_customer_has_name(self):
        self.assertEqual("Princess", self.customer.name)

    def test_customer_has_wallet(self):
        self.assertEqual(20.00, self.customer.wallet)

    def test_customer_makes_payment(self):
        self.drink = Drink("Pina Colada", 4.50)
        self.customer.make_payment(self.drink)
        self.assertEqual(15.50, self.customer.wallet)
