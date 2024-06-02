
from item import Item
#Use inheritance to create a class phone based on item class
class Phone(Item):
    #Call super function in the constructor to have access to all the attributes in the parent class Item
    #these attributes are the name price and quantity. Broken phones are only added to this Phone class
    def __init__(self, name, price, quantity, broken_phones=0):
        super().__init__(name, price, quantity)

