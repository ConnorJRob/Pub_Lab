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

    def find_drink_by_name(self,drink_name):
        # pdb.set_trace()
        for drink in self.drinks:
            if drink.name == drink_name:
                return drink

    def serve_customer(self,customer,drink):
        drink_ordered = self.find_drink_by_name(drink)
        customer.make_payment(drink_ordered)
        self.take_payment(drink_ordered)

