class Item:
    #Initialization of required attributes of an object
    #We can initialize attributes' data type by adding "attribut:datatype"
    def __init__(self, name:str, price:int, quantity:int):
        #Run validations to received attributes
        assert price>=0, f"Price {price} cannot be negative"
        assert quantity>=0, f"Quantity {quantity} cannot be negative"
        
        #Assign attributes to self
        self.name= name
        self.price= price
        self.quantity= quantity

    #Create a method called calculate total price
    def calculateTotalPrice(self):
        totalPrice= self.price * self.quantity
        return totalPrice


item1=Item("Phone", -1,-1)
print(item1.price)
print(item1.calculateTotalPrice())