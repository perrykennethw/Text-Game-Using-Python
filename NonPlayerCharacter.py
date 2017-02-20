from random import *

class Item:

    def __init__(self, name, cost):
        self._name = name
        self._cost = cost

    def get_name(self):
        return self._name

    def get_cost(self):
        return self._cost


class NonPlayerCharacter:

    def __init__(self, name, title, greeting, phrases, location):
        self._name = name
        self._title = title
        self._greeting = greeting
        self._phrases = phrases
        self._location = location
        self._commands = ["greet", "speak", "pay"]
        self._account = 0

    def charge(self, amount):
        self._account += amount

    def greet(self):
        """Return a greeting string."""
        print("I am " + self._name + ", a " + self._title + ". " + self._greeting)

    def speak(self):
        """Return a spoken phrase."""
        #str phrase
        if self._account > 0:
            phrase = "You owe me " + str(self._account) + " gold."
        else:
            phrase = choice(self._phrases)
        print(phrase)

    def get_commands(self):
        """Return the list of commands the npc will respond to."""
        return self._commands

    def get_location(self):
        return self._location
    
    def pay(self):
        """Accept a payment on account, where _account is the amount the PC owes."""
        #int amount
        if self._account > 0:
            amount = int(input("How much would you like to pay? "))
            self._account -= amount
        else:
            print("You don't owe me any money, friend.  Are you making donations?")

    def follow_command(self,command):
        """Follow the specific command."""
        if command == "pay":
            self.pay()
        elif command == "greet":
            self.greet()
        elif command == "speak":
            self.speak()
        else:
            print("I don't know how to do that.")

class Shopkeeper(NonPlayerCharacter):

    def __init__(self, name, title, greeting, phrases, location, inventory):
        super().__init__(name, title, greeting, phrases, location)
        self._commands.append("look")
        self._commands.append("purchase")
        self._inventory = inventory

    def _search_inventory(self, item_name):
        #int index, count
        #list item
        found_item = None
        for item in self._inventory:
            if item.get_name() == item_name:
                found_item = item
        return found_item

    def look(self):
        """A  method that allows the customer to see the shopkeeper's inventory."""
        #list item
        print("Ah, you would like to see my wares!  I have the following items for sale: ")
        for item in self._inventory:
            print(item.get_name()+ " " + str(item.get_cost())+" gold")

    def purchase(self):
        """A  method that allows the customer to purchase from the shopkeeper's inventory."""
        #str item_name
        #int cost
        #Item item
        item_name = input("What would you like to purchase? ")
        item = self._search_inventory(item_name)
        if item != None:
            cost = item.get_cost()
            print("An excellent choice!  That will be "+ str(cost) + " gold.")
            self.charge(cost)
            self._inventory.remove(item)
        else:
            print("I'm sorry, I don't seem to have one of those.")

    def follow_command(self, command):
        """A shopkeeper responds to the look and purchase commands, in addition to superclass commands."""
        if command == "look":
            self.look()
        elif command == "purchase":
            self.purchase()
        else:
            super().follow_command(command)




  
