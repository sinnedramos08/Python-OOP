#Create a new class called Item
class Item:
    pass

#Instantiation of the Item class
item1= Item()

#Create attributes of the Item class

#Method 1: adding attributes outside the class declaration
item1.name="Phone"
item1.price= 100
item1.quantity=5

print(item1.name)
print(item1.price)
print(item1.quantity)

#Create a new class called Person
class Person:
    #New attributes of the person class
    name="Dennis" #This name is the default value

#Instantiate a Person class
person1=Person()

#Access the attribute of name of the person class
print(person1.name)

#Change the default value name of the object person1
person1.name="Andrew"
print(person1.name)


#Create a new class called Place:
class Place:
    #Initialize an object
    def __init__(self, location:str):
        self.location= location

place1=Place("Pasig")
print(place1.location)

