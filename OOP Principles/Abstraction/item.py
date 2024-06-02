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
        #Add double underscore for encapsulation
        #This make the attribute private
        self.__name= name
        self.__price= price
        self.__quantity= quantity

    #Making price read only 
    @property
    def price(self):
        print("Price is a read only attribute")
        return self.__price


    #Define a method that will apply a discount to the price
    def discountedPrice(self):
        #Overwrite the new price with this 
        self.__price = self.__price* self.discount
        return self.__price
    

    #Abstraction Example
    #add double underscore to make the hidden method
    #We can only access these subtasks within the class
    def __connect(self, smpt_server):
        pass
    def ___make_body(self):
        #Make the body of email here:
        pass
    def __send(self):
        pass

    def send_email(self):
        #Subtask that are not needed to be exposed
        self.__connect("XXXX")
        self.___make_body()
        self.__send()
