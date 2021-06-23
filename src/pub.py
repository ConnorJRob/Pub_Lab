class Pub:
    def __init__(self, name, till, drinks):
        self.name = name
        self.till = till
        self.drinks = drinks

    def take_payment(self,amount):
        self.till += amount

class Drinks:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class Customer:
    def __init__(self, name, wallet):
        self.name = name
        self.wallet = wallet