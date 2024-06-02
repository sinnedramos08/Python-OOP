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

    #Instantiate from a csv file
    
    #Note that, we can not use the self as a parameter here since we wont be 
    #using this method with an object instance, instead we will use it to instantiate
    #the class itself

    #Use class method
    #Instead of self, we use cls
    @classmethod
    def instantiate_from_csv(cls):
        
        with open(r"C:\Users\denni\OneDrive\Desktop\Coding\Python\OOP\Python-OOP\Others\item.csv","r") as file:
            content=csv.DictReader(file, delimiter=",") #Create a Dictreader object based on the csv file
            items=list(content) #Put the content into a list, each element are dictionaries: 
            #Output: [{'name': 'Phone', ' price': ' 5000', ' quantity': ' 1'}, {'name': 'Laptop', ' price': ' 10000', ' quantity': ' 1'}, {'name': 'Cable', ' price': ' 50', ' quantity': ' 3'}, {'name': 'Mouse', ' price': ' 500', ' quantity': ' 3'}, {'name': 'Keyboard', ' price': ' 1000', ' quantity': ' 3'}]
            
            for item in items:
                #instantiate the instances using the list
                #When you call this method using the class, it will iterate over the items list and create a new instance based on the list
                Item(
                    name=item.get("name"),
                    price=int(item.get("price")),
                    quantity=int(item.get("quantity"))
                )


    #For representing objects
    #This make the debugging easier since the 
    #Represntations are readable
    def __repr__(self):
        return f"Item({self.name}, {self.price}, {self.discount})"
    
#Instantiate the class using the csv
#Unlike instantiating the object by using "variable=Item()", we instead use the defined class method
#to instantiate the class
Item.instantiate_from_csv()
print(Item.all)