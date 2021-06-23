class Customer:
    def __init__(self, name, wallet):
        #Customer Class is established and requires a name (string) and wallet amount (float) to initliase
        self.name = name
        self.wallet = wallet

    #This function allows the customer to decrease the value of the self.wallet property by the price property of the drink object given as an argument
    def make_payment(self, drink):
        self.wallet -= drink.price