import pdb

class Pub:
    def __init__(self, name, till):
        self.name = name
        self.till = till
        self.drinks = []

    def take_payment(self,drink):
        self.till += drink.price

    def add_drink_to_menu(self,drink):
        self.drinks.append(drink)