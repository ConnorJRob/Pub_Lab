import unittest
from src.pub import *
from src.drink import *
from src.customer import *

class TestPub(unittest.TestCase):

    def setUp(self):
        self.customer = Customer("Princess", 20)

    def test_customer_has_name(self):
        self.assertEqual("Princess", self.customer.name)
        
    def test_has_wallet(self):
        self.assertEqual(20, self.customer.wallet)
    
    def test_decrease_wallet(self):
        self.customer.make_payment(5)
        self.assertEqual(15, self.customer.wallet)

