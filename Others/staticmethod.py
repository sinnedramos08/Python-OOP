import csv

class Item:
    #Class Attribute
    discount=0.8
    all=[] #Create a Class attribute with a list type

    #Initialization of required attributes of an object
    #We can initialize attributes' data type by adding "attribut:datatype"
    def __init__(self, name:str, price:int, quantity:int):
        #Run validations to received attributes
        assert price>=0, f"Price {price} cannot be negative"
        assert quantity>=0, f"Quantity {quantity} cannot be negative"
        
        #Instance Attribute
        #Assign attributes to self
        self.name= name
        self.price= price
        self.quantity= quantity

        '''
        When creating a new instance, 
        we append it to the all list which
        is a class attribute by passing self
        when appending
        '''
        Item.all.append(self)

    #Define a method that will apply a discount to the price
    def discountedPrice(self):
        #Overwrite the new price with this 
        self.price = self.price* self.discount
        return self.price

    #Static Method
    #Static method does not pass self attribute unlike other methods in class that uses self (which is the object itself)
    #Just a regular function inside a class
    @staticmethod
    def is_integer(num):
        #Check and cout for float values of num
        if isinstance(num, float): #isintance function checks if the first parameter (num) is an instance of the second parameter (float)
            #Returns true or false
            return num.is_integer()
        elif isinstance(num, int):
            return True
        else:
            return False

    #For representing objects
    #This make the debugging easier since the 
    #Represntations are readable
    def __repr__(self):
        return f"Item({self.name}, {self.price}, {self.discount})"
    
#We use the static methiod like this:
print(Item.is_integer(7.5))