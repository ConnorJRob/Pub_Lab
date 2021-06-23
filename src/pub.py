import pdb

class Pub:
    def __init__(self, name, till):
        #Pub Class is established and requires a name (string) and till amount (float) to initliase
        self.name = name
        self.till = till
        self.drinks = []
        #The properties of the Pub Class are established using the name and till amount given.
        #An empty drinks list is also created

    #This function allows the pub to increase the value of the self.till property by the price property of the drink object given as an argument
    def take_payment(self,drink):
        self.till += drink.price

    #This function allows drinks objects to be appended onto the self.drinks list
    def add_drink_to_menu(self,drink):
        self.drinks.append(drink)

    #This function takes a string (the name of a drink ideally) and searches through the self.drinks list for a drink object that has a name property matching the string given
    #If found then the function returns the drink object that has a matching name property
    def find_drink_by_name(self,drink_name):
        # pdb.set_trace()
        for drink in self.drinks:
            if drink.name == drink_name:
                return drink

    #This function takes a customer object and a drink name string, it then uses the drink name string given and runs the find_drink_by_name function above
    def serve_customer(self,customer,drink_name):
        drink_ordered = self.find_drink_by_name(drink_name)
        #The value returned by this function is stored in 'drink_ordered'
        customer.make_payment(drink_ordered)
        #The make_payment function is called from the customer class and given the drink_ordered variable, this removes the price of the drink ordered from the customers wallet property 
        self.take_payment(drink_ordered)
        #The take_payment function is called and given the drink_ordered variable, this adds the price of the drink ordered to the pubs till property

