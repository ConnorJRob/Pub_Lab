import unittest
from src.pub import *
from src.drink import *
from src.customer import *

class TestPub(unittest.TestCase):
    
    def setUp(self):
        #The test is set up with the below Pub class which will be the case at the beginning of every test
        self.pub = Pub("The Yawning Portal", 100.00)

    def test_pub_has_name(self):
        #This test checks that given the Pub Class created above, the pub.name property has been correctly setup matching "The Yawning Portal"
        self.assertEqual("The Yawning Portal", self.pub.name)

        #This test checks that given the Pub Class created above, the pub.till property has been correctly setup matching 100.00
    def test_pub_has_till(self):
        self.assertEqual(100, self.pub.till)

        #This test checks that given the Pub Class created above, the pub.drinks property has been correctly setup, i.e the list exists but is empty
    def test_pub_has_drinks_list(self):
        self.assertEqual([], self.pub.drinks)

        #This test checks that a drink has been added to the drinks list by the add_drink_to_menu function
    def test_drinks_added_to_menu(self):
        #As part of this test a drink object is created using the Drink Class and this is assigned to self.drink
        self.drink = Drink("Pina Colada", 4.50)
        #The add_drink_to_menu function is called from the Pub Class and is given the self.drink variable established
        self.pub.add_drink_to_menu(self.drink)
        #To test that this worked, the test line checks the length of the pub.drinks property. It started at 0, so if the add_drink_to_menu function has worked correctly, it's length should now be 1
        self.assertEqual(1, len(self.pub.drinks))

        #This test checks that the value of the pub.till property is increased appropriately once the pub.take_payment function is run
    def test_pub_takes_payment(self):
        #As part of this test a drink object is created using the Drink Class and this is assigned to self.drink
        self.drink = Drink("Pina Colada", 4.50)
        #The take_payment function is called from the Pub Class and is given the self.drink variable established
        self.pub.take_payment(self.drink)
        #To test that this worked, the test line checks the value of the pub.till property is equal to the original starting value + the price of the self.drink variable provided
        self.assertEqual(104.50, self.pub.till)

        #This test checks that the find_drink_by_name function is working correctly and returning the drink object with a name property matching the string given as an argument
    def test_find_drink_by_name(self):
        #As part of this test 3 drink objects are created using the Drink Class and these are assigned to self.drink 1, 2 & 3
        self.drink1 = Drink("Pina Colada", 4.50)
        self.drink2 = Drink("Mai Thai", 5.00)
        self.drink3 = Drink("Sex on the Beach", 3.50)
        #Using the add_drink_to_menu function, the above drinks are all added to the currently blank pub.drinks list
        self.pub.add_drink_to_menu(self.drink1)
        self.pub.add_drink_to_menu(self.drink2)
        self.pub.add_drink_to_menu(self.drink3)
        #The find_drink_by_name function is run with a drink name given as a variable, the result of this function is stored in the searched_drink variable
        searched_drink = self.pub.find_drink_by_name("Sex on the Beach")
        #To test that this has worked, the test list checks that the name of the drink object returned by the above function matches the string that was given as the drink name search criteria
        self.assertEqual("Sex on the Beach", searched_drink.name)

    #This test checks that the serve customer function is working correctly by checking the value of both the customer wallet and pub till once the function is complete
    def test_serve_customer(self):
        #As part of this test a customer object is created using the Customer Class and this is assigned to customer
        customer = Customer("Princess", 20.00)
        #As part of this test 3 drink objects are created using the Drink Class and these are assigned to self.drink 1, 2 & 3
        self.drink1 = Drink("Pina Colada", 4.50)
        self.drink2 = Drink("Mai Thai", 5.00)
        self.drink3 = Drink("Sex on the Beach", 3.50)
        #Using the add_drink_to_menu function, the above drinks are all added to the currently blank pub.drinks list
        self.pub.add_drink_to_menu(self.drink1)
        self.pub.add_drink_to_menu(self.drink2)
        self.pub.add_drink_to_menu(self.drink3)
        #The serve customer function is called, with the established customer variable and drink name string given as arguments
        self.pub.serve_customer(customer, "Mai Thai")
        #The test line then checks that the value of the customers wallet has reduced by the price of the searched drink, and the pub's till has increase by the price of the searched drink
        self.assertEqual(15, customer.wallet)
        self.assertEqual(105, self.pub.till)
    

                    #This is some code we played with in testing
                                # self.assertEqual(3, len(self.pub.drinks))
                                 # self.pub.find_drink_by_name("Sex on the Beach")
                                 # self.assertEqual("Sex on the Beach", drink.name)

                                # thislist = ["apple", "banana", "cherry"]
                                # # thislist.append("orange")
                                # print(thislist)
