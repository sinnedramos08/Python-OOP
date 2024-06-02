from item import Item
class Laptop(Item):
    def __init__(self, name, price, quantity):
        super().__init__(name, price, quantity)