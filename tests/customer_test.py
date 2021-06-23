import unittest
from src.drink import *
from src.customer import *

class TestCustomer(unittest.TestCase):

    def setUp(self):
        #The test is set up with the below Customer class which will be the case at the beginning of every test
        self.customer = Customer("Princess", 20.00)

    def test_customer_has_name(self):
        #This test checks that given the Customer Class created above, the customer.name property has been correctly setup matching "Princess"
        self.assertEqual("Princess", self.customer.name)

    def test_customer_has_wallet(self):
        #This test checks that given the Customer Class created above, the customer.wallet property has been correctly setup matching 20
        self.assertEqual(20.00, self.customer.wallet)

        #This test checks that the value of the pub.till property is increased appropriately once the pub.take_payment function is run
    def test_customer_makes_payment(self):
        #As part of this test a drink object is created using the Drink Class and this is assigned to self.drink
        self.drink = Drink("Pina Colada", 4.50)
        #The make_payment function is called from the Customer Class and is given the self.drink variable established
        self.customer.make_payment(self.drink)
        #To test that this worked, the test line checks the value of the customer.wallet property is equal to the original starting value - the price of the self.drink variable provided
        self.assertEqual(15.50, self.customer.wallet)
