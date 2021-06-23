import unittest
from src.pub import *
from src.drink import *
from src.customer import *

class TestPub(unittest.TestCase):
    
    def setUp(self):
        self.pub = Pub("The Yawning Portal", 100.00)

    def test_pub_has_name(self):
        self.assertEqual("The Yawning Portal", self.pub.name)

    def test_pub_has_till(self):
        self.assertEqual(100, self.pub.till)

    def test_pub_has_drinks_list(self):
        self.assertEqual([], self.pub.drinks)

    def test_drinks_added_to_menu(self):
        self.drink = Drink("Pina Colada", 4.50)
        self.pub.add_drink_to_menu(self.drink)
        self.assertEqual(1, len(self.pub.drinks))

    def test_pub_takes_payment(self):
        self.drink = Drink("Pina Colada", 4.50)
        self.pub.take_payment(self.drink)
        self.assertEqual(104.50, self.pub.till)

    # def test_can_find_drink_by_name(self):
    #     self.drink1 = Drink("Pina Colada", 4.50)
    #     self.drink2 = Drink("Mai Thai", 5.00)
    #     self.drink3 = Drink("Sex on the Beach", 3.50)
    #     self.pub.add_drink_to_menu(self.drink1)
    #     self.pub.add_drink_to_menu(self.drink2)
    #     self.pub.add_drink_to_menu(self.drink3)
    #                            # self.assertEqual(3, len(self.pub.drinks))
    #     self.pub.find_drink_by_name("Sex on the Beach")
    #     self.assertEqual("Sex on the Beach", drink.name)

                                # thislist = ["apple", "banana", "cherry"]
                                # # thislist.append("orange")
                                # print(thislist)
