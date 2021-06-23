import unittest
from src.pub import *

class TestPub(unittest.TestCase):
    
    def setUp(self):
        self.pub = Pub("The Yawning Portal", 100.00, [])
        self.customer = Customer("Princess", 20)

    def test_pub_has_name(self):
        self.assertEqual("The Yawning Portal", self.pub.name)

    def test_increase_till(self):
        self.pub.take_payment(10)
        self.assertEqual(110, self.pub.till)

    def test_decrease_wallet(self):
        self.customer.make_payment(5)
        self.assertEqual(15, self.customer.wallet)