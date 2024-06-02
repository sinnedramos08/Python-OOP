class Item:
    #Class Attribute
    discount=0.8 

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

    #Define a method that will apply a discount to the price
    def discountedPrice(self):
        #Overwrite the new price with this 
        self.price = self.price* self.discount
        return self.price

item1=Item("Phone", 5000, 5)
#Access the class attribute using class itself
print(Item.discount)

#Access the class attribute using the object instance
print(item1.discount)

#Use the discountedPrice method
print("Discounted Price",item1.discountedPrice())

#See if item1 price is overwritten by using the method
print("Overwritten Price", item1.price)