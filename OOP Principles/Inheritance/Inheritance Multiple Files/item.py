class Item:
    discount=0.8
    all_items=[]
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
        Item.all_items.append(self)

    #Define a method that will apply a discount to the price
    def discountedPrice(self):
        #Overwrite the new price with this 
        self.price = self.price* self.discount
        return self.price

    #For representing objects
    #This make the debugging easier since the 
    #Represntations are readable
    def __repr__(self):
        return f"{self.__class__.__name__}({self.name}, {self.price}, {self.discount})"